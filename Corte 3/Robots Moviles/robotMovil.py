import numpy as np
import math
import pygame
import sympy as sym
import matplotlib.pyplot as plt

class Environment:
    def __init__(self, dimentions):
        # colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)

        # Dimensiones mapa
        self.height = dimentions[0]
        self.width = dimentions[1]
        
        # Configuracion ventana/Window
        pygame.display.set_caption("Robot Diferencial")
        self.map = pygame.display.set_mode( (self.width, self.height) )

        # Text Variables
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.text = self.font.render('default', True, self.white, self.black)
        self.textRect = self.text.get_rect()
        self.textRect.center = (dimentions[1]-600, dimentions[0]-100)
        self.trail_set = []
    
    def write_info(self, VLeft, VRight, theta):
        txt = f"VLeft = {VLeft} VRight = {VRight} theta = {int(math.degrees(theta))}"
        self.text = self.font.render(txt, True, self.white, self.black)
        self.map.blit(self.text, self.textRect)

    def trail(self, pos):
        for i in range(0, len(self.trail_set)-1 ):
            pygame.draw.line( self.map, self.yellow, (self.trail_set[i][0], self.trail_set[i][1]), (self.trail_set[i+1][0], self.trail_set[i+1][1]) )
        
        if self.trail_set.__sizeof__() > 10000:
            self.trail_set.pop(0)
        self.trail_set.append(pos)
    
    def robot_frame(self, pos, rotation):
        n = 80

        centerX, centerY = pos
        x_axis = (centerX + n*math.cos(-rotation), centerY + n*math.sin(-rotation) )
        y_axis = (centerX + n*math.cos(-rotation + math.pi/2), centerY + n*math.sin(-rotation + math.pi/2) )

        pygame.draw.line(self.map, self.red, (centerX, centerY), x_axis, 3)
        pygame.draw.line(self.map, self.green, (centerX, centerY), y_axis, 3)

        

class Robot():
    def __init__(self, startpos, robotImg, width):
        
        #Conversion de metros a pixeles
        self.meter2pixel = 3779.52

        # Dimensiones Robot
        self.width = width
        self.x = startpos[0]
        self.y = startpos[1]
        self.theta = 0
        self.vLeft = 0.01*self.meter2pixel # m/s
        self.vRight = 0.01*self.meter2pixel # m/s
        self.maxSpeed = 0.02*self.meter2pixel
        self.minSpeed = 0.02*self.meter2pixel

        # Graficos
        self.img = pygame.image.load('Corte 3\Robots Moviles\DDR.png')
        self.rotated = self.img
        self.rect = self.rotated.get_rect(center =(self.x,self.y))

    def draw(self, map):
        map.blit(self.rotated, self.rect)
    
    def move(self, event = None):
        if event is not None:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP4:
                    self.vLeft += 0.001*self.meter2pixel
                elif event.key == pygame.K_KP1:
                    self.vLeft -= 0.001*self.meter2pixel
                elif event.key == pygame.K_KP6:
                    self.vRight += 0.001*self.meter2pixel
                elif event.key == pygame.K_KP3:
                    self.vRight -= 0.001*self.meter2pixel
        
        self.x += ((self.vLeft + self.vRight)/2)*math.cos(self.theta)*dt
        self.y -= ((self.vLeft + self.vRight)/2)*math.sin(self.theta)*dt
        self.theta += (self.vRight - self.vLeft)/self.width*dt

        # Reiniciar theta
        if self.theta > 2*math.pi or self.theta < -2*math.pi:
            self.theta = 0
        
        # velocidad maxima
        self.vRight = min(self.vRight, self.maxSpeed)
        self.vLeft = min(self.vLeft, self.maxSpeed)

        # velocidad minima
        self.vRight = max(self.vRight, self.minSpeed)
        self.vLeft = max(self.vLeft, self.minSpeed)


        self.rotated = pygame.transform.rotozoom(self.img, math.degrees(self.theta), 1)
        self.rect = self.rotated.get_rect(center=(self.x, self.y))
        





# Inicizalizacion
pygame.init()

# Coordenadas Iniciales
start = (200, 200)


# Dimensiones
dims = (600, 1300)

# Running or Not
running = True

# Entorno/Environmentonment
environment = Environment(dims)

# Definimos el Robot
robot = Robot(start, r"C:\Users\Juan Jose Restrepo\Desktop\Robotics\Corte 3\Robots Moviles\DDR.png", 0.01*3779.52)

# dt
dt = 0
lastTime = pygame.time.get_ticks()

# Bucle Simulacion
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        robot.move(event)
    
    dt = (pygame.time.get_ticks()-lastTime)/1000
    lastTime = pygame.time.get_ticks()
    pygame.display.update()
    environment.map.fill(environment.black)
    robot.move()
    environment.write_info(int(robot.vLeft),
                           int(robot.vRight),
                           robot.theta)
    robot.draw(environment.map)
    environment.robot_frame( (robot.x, robot.y), robot.theta)
    environment.trail( (robot.x, robot.y) )
