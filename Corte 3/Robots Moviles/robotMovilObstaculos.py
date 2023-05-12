import pygame
import math
import numpy as np

def calcularDistancia(punto1, punto2):
    punto1 = np.array(punto1)
    punto2 = np.array(punto2)
    return np.linalg.norm(punto1 - punto2)

class Robot:
    def __init__(self, posInicial, width):

        #Conversion de metros a pixeles
        self.meter2pixel = 3779.52

        # Dimensiones Robot
        self.width = width
        self.x = posInicial[0]
        self.y = posInicial[1]

        # Direccion/Rumbo/theta/theta
        self.theta = 0 

        # Velocidades Eje Izquierdo y Derecho
        # pixeles a metros por segundo (m/s)
        # 0.01* -> 1cm/s
        self.vel_Left = 0.01*self.meter2pixel
        self.vel_Right = 0.01*self.meter2pixel

        # Velocidad maxima y minima
        self.maxSpeed = 0.02*self.meter2pixel
        self.minSPeed = 0.01*self.meter2pixel

        # distancia minima robot
        self.dist_min_obstaculo = 100

        # Contador diferencial de tiempo dt
        self.countDown = 5 # segundos

    # dt: time step
    def evadirObstaculo(self, nubePuntos, dt):
        obstaculo_mas_cercano = None
        distancia_actual_objeto = np.inf

        if len(nubePuntos) > 1:
            for punto in nubePuntos:
                if distancia_actual_objeto > calcularDistancia( [self.x, self.y], punto ):
                    distancia_actual_objeto = calcularDistancia([self.x, self.y], punto)
                    obstaculo_mas_cercano = (punto, distancia_actual_objeto)
            
            if obstaculo_mas_cercano[1] < self.dist_min_obstaculo and self.countDown > 0:
                self.countDown -= dt
                self.move_backwards()
            else:
                # Reiniciamos el contador de tiempo
                self.countDown = 5

                # Mover hacia adelante
                self.move_forward()
    

    def move_backwards(self):
        self.vel_Right = - self.minSPeed
        self.vel_Left = - self.minSPeed/2

    def move_forward(self):
        self.vel_Right = self.minSPeed
        self.vel_Left = self.minSPeed

    def cinematica(self, dt):
        self.x += ((self.vel_Left + self.vel_Right)/2) * math.cos(self.theta) * dt
        self.y -= ((self.vel_Left + self.vel_Right)/2) * math.sin(self.theta) * dt
        self.theta += (self.vel_Right - self.vel_Left) / self.width * dt

        if self.theta > 2*math.pi or self.theta < -2*math.pi:
            self.theta = 0
    
        self.vel_Right = max( min(self.maxSpeed, self.vel_Right), self.minSPeed )
        self.vel_Left = max( min(self.maxSpeed, self.vel_Left), self.minSPeed )

class Entorno:
    def __init__(self, dimensiones, robot_img_path, map_img_path):
        pygame.init()

        # Colores
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)

        # ----- MAPA ------

        # Cargar Imagenes
        self.robot = pygame.image.load(robot_img_path)
        self.imagen_mapa = pygame.image.load(map_img_path)

        # dimensiones
        self.height, self.width = dimensiones

        # configuracion de la ventana/window
        pygame.display.set_caption("Robot Movil Evasor Obstaculos")
        self.map = pygame.display.set_mode( (self.width, self.height) )
        self.map.blit(self.imagen_mapa, (0, 0) )

    def dibujarRobot(self, x, y, theta):
        rotated = pygame.transform.rotozoom(self.robot, math.degrees(theta), 1)
        rect = rotated.get_rect( center=(x, y) )
        self.map.blit(rotated, rect)
    
    def showDataSensor(self, nubePuntos):
        for punto in nubePuntos:
            pygame.draw.circle(self.map, self.red, punto, 3, 0)


class Ultrasonido:

    def __init__(self, rango_sensor, map):
        self.rango_sensor = rango_sensor
        self.map_width, self.map_height = pygame.display.get_surface().get_size()
        self.map = map

    def sensarObstaculo(self, x, y, theta):
        obstaculos = []
        x1, y1 = x, y
        angulo_inicio = theta - self.rango_sensor[1]
        angulo_final = theta + self.rango_sensor[1]
        for angulo in np.linspace(angulo_inicio, angulo_final, 10, False):
            x2 = x1 + self.rango_sensor[0] * math.cos(angulo)
            y2 = y1 - self.rango_sensor[0] * math.sin(angulo)
            for i in range(0, 100):
                u = i/100
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u))
                if 0 < x < self.map_width and 0 < y < self.map_height:
                    color = self.map.get_at( (x, y) )
                    self.map.set_at( (x, y), (0, 208, 255) )
                    if (color[0], color[1], color[2]) == (0, 0, 0): # si el color es negro
                        obstaculos.append( [x, y] )
                        break
        
        return obstaculos


