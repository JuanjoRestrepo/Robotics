import math
import pygame
from robotMovilObstaculos import Entorno, Robot, Ultrasonido


DIMENSIONES_MAPA = (600, 1200)

# ENVIRONMENT
#graficos = Entorno(DIMENSIONES_MAPA, 'Corte 3\Robots Moviles\DDR.png', 'Corte 3\Robots Moviles\mapa.png')
graficos = Entorno(DIMENSIONES_MAPA, '/Users/jorgerestrepo/Desktop/Robotics/Corte 3/Robots Moviles/DDR.png', '/Users/jorgerestrepo/Desktop/Robotics/Corte 3/Robots Moviles/mapa.png')

# Robot
posInicial = (200, 330)
robot = Robot(posInicial, 0.01*3779.52)

# Sensor Ultrasonico
rango_sensor = 250, math.radians(40)
ultrasonido = Ultrasonido(rango_sensor, graficos.map)




dt = 0
last_time = pygame.time.get_ticks()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = (pygame.time.get_ticks() - last_time )/1000
    last_time = pygame.time.get_ticks()

    graficos.map.blit(graficos.imagen_mapa, (0,0) )

    robot.cinematica(dt)
    graficos.dibujarRobot(robot.x, robot.y, robot.theta)
    nubePuntos = ultrasonido.sensarObstaculo(robot.x, robot.y, robot.theta)

    robot.evadirObstaculo(nubePuntos, dt)
    graficos.showDataSensor(nubePuntos)

    pygame.display.update()
