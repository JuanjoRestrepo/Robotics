import pygame
import math
import numpy as np

# Se define una función que calcula la distancia entre dos puntos
def calcularDistancia(punto1, punto2):
    punto1 = np.array(punto1)
    punto2 = np.array(punto2)
    return np.linalg.norm(punto1 - punto2)

# se define la clase Robot que contiene toda la información y comportamiento del robot móvil.
class Robot:

    #Se define el constructor de la clase Robot. 
    # Se inicializan las variables de posición, dirección, velocidad, dimensiones y límites de velocidad.
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

    # Se define la función evadirObstaculo que se encarga de detectar y evitar obstáculos. ]
    # Se recibe una nube de puntos (nubePuntos) y un intervalo de tiempo (dt).
    # dt: time step
    def evadirObstaculo(self, nubePuntos, dt):
        obstaculo_mas_cercano = None
        distancia_actual_objeto = np.inf

        # Se calcula el punto más cercano dentro de la nube de puntos. 
        # Si la distancia entre el robot y el obstáculo es menor a una distancia límite (dist_min_obstaculo) y el contador
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
    
    # Las funciones move_forward() y move_backwards() 
    # se encargan de definir las velocidades de las ruedas del robot para que este se mueva hacia adelante o hacia atrás
    # La velocidad de la rueda derecha se asigna a self.vel_Right 
    # La velocidad de la rueda izquierda se asigna a self.vel_Left.
    def move_backwards(self):
        self.vel_Right = - self.minSPeed
        self.vel_Left = - self.minSPeed/2

    def move_forward(self):
        self.vel_Right = self.minSPeed
        self.vel_Left = self.minSPeed

    # La función cinematica(dt) actualiza la posición y orientación del robot utilizando las velocidades de las ruedas
    def cinematica(self, dt):
        # se calcula el cambio en la posición en el eje x (self.x) y el eje y (self.y) utilizando la ecuacion de la cinemática diferencial.
        self.x += ((self.vel_Left + self.vel_Right)/2) * math.cos(self.theta) * dt
        self.y -= ((self.vel_Left + self.vel_Right)/2) * math.sin(self.theta) * dt
        # se actualiza la orientación (self.theta) utilizando la ecuacion de la cinemática diferencial.
        self.theta += (self.vel_Right - self.vel_Left) / self.width * dt

        # se verifica si el ángulo de orientación (self.theta) ha superado el valor de 2pi o -2pi, que son equivalentes a un giro completo de 360 grados.
        if self.theta > 2*math.pi or self.theta < -2*math.pi:
            # Si este es el caso, se reinicia el ángulo de orientación a cero.
            self.theta = 0

        # se asegura que la velocidad de cada rueda no supere la velocidad máxima (self.maxSpeed) 
        # ni sea menor que la velocidad mínima (self.minSPeed
        self.vel_Right = max( min(self.maxSpeed, self.vel_Right), self.minSPeed )
        self.vel_Left = max( min(self.maxSpeed, self.vel_Left), self.minSPeed )


# Clase Entorno que crea la ventana de visualización del robot y carga las imágenes del mapa y el robot.
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

    #  Dibuja el robot en la ventana, a partir de las coordenadas x e y y el ángulo theta 
    def dibujarRobot(self, x, y, theta):
        # rota la imagen del robot usando la función pygame.transform.rotozoom 
        # y luego la dibuja en la ventana con la función self.map.blit
        rotated = pygame.transform.rotozoom(self.robot, math.degrees(theta), 1)
        rect = rotated.get_rect( center=(x, y) )
        self.map.blit(rotated, rect)
    
    # Dibuja en la ventana los puntos obtenidos por el sensor de ultrasonido. 
    # Cada punto se dibuja como un círculo rojo
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

                # Si la posición del punto calculado está dentro de los límites de la ventana, 
                # se consulta el color de píxel de la imagen del mapa en esa posición. 
                if 0 < x < self.map_width and 0 < y < self.map_height:

                    # Además, el píxel se dibuja con un color azul claro (0, 208, 255) 
                    # para simular y marcar los puntos que han sido evaluados por el sensor.
                    color = self.map.get_at( (x, y) )
                    self.map.set_at( (x, y), (0, 208, 255) )

                    # si el color es negro entonces se interpreta que hay un obstáculo 
                    # y se agrega la posición del obstáculo a una lista
                    if (color[0], color[1], color[2]) == (0, 0, 0): 
                        obstaculos.append( [x, y] )
                        break
        
        # Retorna una lista de coordenadas de los obstáculos detectados
        return obstaculos


