import numpy as np
import matplotlib.pyplot as plt

'''
a1 = float(input("Ingrese el largo del eslabon (a1) en mm: "))
tethaR1 = float(input("Ingrese el ángulo de la articulación en grados (theta1): "))
b1 = float(input("Ingrese el desplazamiento que desea hacer en el eje Z (b1) en mm: "))
alphaR1 = float(input("Ingrese el ángulo de rotación en grados (alpha1): "))

print("\n")

a2 = float(input("Ingrese el largo del eslabon (a2) en mm: "))
tethaR2 = float(input("Ingrese el ángulo de la articulación en grados (theta2): "))
b2 = float(input("Ingrese el desplazamiento que desea hacer en el eje Z (b2) en mm: "))
alphaR2 = float(input("Ingrese el ángulo de rotación en grados (alpha2): "))

print("\n")

a3 = float(input("Ingrese el largo del eslabon (a3) en mm: "))
tethaR3 = float(input("Ingrese el ángulo de la articulación en grados (theta3): "))
b3 = float(input("Ingrese el desplazamiento que desea hacer en el eje Z (b3) en mm: "))
alphaR3 = float(input("Ingrese el ángulo de rotación en grados (alpha3): "))
'''
a1 = 200
tethaR1 = 45
b1 = 0
alphaR1 = 0

a2 = 150
tethaR2 = -45
b2 = 0
alphaR2 = 0

a3 = 50
tethaR3 = -90
b3 = 0
alphaR3 = 0

tetha1 = (tethaR1*np.pi)/180
alpha1 = (alphaR1*np.pi)/180

tetha2 = (tethaR2*np.pi)/180
alpha2 = (alphaR2*np.pi)/180

tetha3 = (tethaR3*np.pi)/180
alpha3 = (alphaR3*np.pi)/180

Tb1 = [[1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, b1],
      [0, 0, 0, 1]]

Tb2 = [[1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, b2],
      [0, 0, 0, 1]]

Tb3 = [[1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, b3],
      [0, 0, 0, 1]]

Ttetha1 = [[np.cos(tetha1), -np.sin(tetha1), 0, 0],
          [np.sin(tetha1), np.cos(tetha1), 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]]

Ttetha2 = [[np.cos(tetha2), -np.sin(tetha2), 0, 0],
          [np.sin(tetha2), np.cos(tetha2), 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]]
Ttetha3 = [[np.cos(tetha3), -np.sin(tetha3), 0, 0],
          [np.sin(tetha3), np.cos(tetha3), 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]]

Ta1 = [[1, 0, 0, a1],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]

Ta2 = [[1, 0, 0, a2],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]

Ta3 = [[1, 0, 0, a3],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]

Talpha1 = [[1, 0, 0, 0],
         [0, np.cos(alpha1), -np.sin(alpha1), 0],
          [0, np.sin(alpha1), np.cos(alpha1), 0],
          [0, 0, 0, 1]]

Talpha2 = [[1, 0, 0, 0],
         [0, np.cos(alpha2), -np.sin(alpha2), 0],
          [0, np.sin(alpha2), np.cos(alpha2), 0],
          [0, 0, 0, 1]]

Talpha3 = [[1, 0, 0, 0],
         [0, np.cos(alpha3), -np.sin(alpha3), 0],
          [0, np.sin(alpha3), np.cos(alpha3), 0],
          [0, 0, 0, 1]]

T1_1 = np.dot(Tb1, Ttetha1)
T1_2 = np.dot(T1_1, Ta1)
T1_a_0 = np.dot(T1_2, Talpha1)

print("\nMatriz de Transformacion T1 -> 0 (TL1): (a1 = {} mm, b1 = {}, tetha1 = {}°, alpha1 = {}°)\n\n" .format(a1, b1, tethaR1, alphaR1), np.matrix(T1_a_0).round(3) )

T2_1 = np.dot(Tb2, Ttetha2)
T2_2 = np.dot(T2_1, Ta2)
T2_a_1 = np.dot(T2_2, Talpha2)
print("\nMatriz de Transformacion T2 -> 1 (TL2): (a2 = {} mm, b2 = {}, tetha2 = {}°, alpha2 = {}°)\n".format(a2, b2, tethaR2, alphaR2), np.matrix(T2_a_1).round(3) )

T3_1 = np.dot(Tb3, Ttetha3)
T3_2 = np.dot(T3_1, Ta3)
T3_a_2 = np.dot(T3_2, Talpha3)
print("\nMatriz de Transformacion T3 -> 2 (TL3): (a3 = {} mm, b3 = {}, tetha3 = {}°, alpha3 = {}°)\n\n".format(a3, b3, tethaR3, alphaR3), np.matrix(T3_a_2).round(3)  )

T10_21 = np.dot(T1_a_0, T2_a_1)
Tfinal = np.dot(T10_21, T3_a_2)
print("\nMatriz de Transformacion TF (0 -> 3):\n\n", np.matrix(Tfinal).round(3) )

#P3 = Tfinal[:3,3].reshape(3,-1)
P3 = Tfinal[:3,3]
print("\nP3: ", P3 )
