import numpy as np

a = float(input("Ingrese por favor el largo del eslabon (a): "))
tethaR = float(input("Ingrese por favor el ángulo de la articulación en grados (theta): "))
b = float(input("Ingrese por favor el desplazamiento que desea hacer en el eje z (b): "))
alphaR = float(input("Ingrese por favor el ángulo de rotación en grados (alpha): "))

tetha = (tethaR*np.pi)/180
alpha = (alphaR*np.pi)/180

Tb = [[1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, b],
      [0, 0, 0, 1]]
print("\nMatriz Tb:\n", np.matrix(Tb))

Ttetha = [[np.cos(tetha), -np.sin(tetha), 0, 0],
          [np.sin(tetha), np.cos(tetha), 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]]
print("\nMatriz Ttetha:\n", np.matrix(Ttetha))

Ta = [[1, 0, 0, a],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]
print("\nMatriz Ta:\n", np.matrix(Ta))

Talpha = [[1, 0, 0, 0],
         [0, np.cos(alpha), -np.sin(alpha), 0],
          [0, np.sin(alpha), np.cos(alpha), 0],
          [0, 0, 0, 1]]
print("\nMatriz Talpha:\n", np.matrix(Talpha))

T1 = np.dot(Tb, Ttetha)
T2 = np.dot(Ta, Talpha)
T = np.dot(T1, T2)

print("\nMatriz de Transformacion:\n", T)
