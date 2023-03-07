import numpy as np
import matplotlib.pyplot as plt

b1 = 0
tetha1R = 45
a1 = 200
alpha1R = 0

b2 = 0
tetha2R = -45 
a2 = 150
alpha2R = 0

b3 = 0
tetha3R = -90
a3 = 50
alpha3R = 0

tetha1 = (tetha1R*np.pi)/180
alpha1 = (alpha1R*np.pi)/180

tetha2 = (tetha2R*np.pi)/180
alpha2 = (alpha2R*np.pi)/180

tetha3 = (tetha3R*np.pi)/180
alpha3 = (alpha3R*np.pi)/180

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

print("\nMatriz de Transformacion T1 -> 0 (TL1): (a1 = {} mm, b1 = {}, tetha1 = {}°, alpha1 = {}°)\n\n" .format(a1, b1, tetha1R, alpha1R), np.matrix(T1_a_0).round(3) )

T2_1 = np.dot(Tb2, Ttetha2)
T2_2 = np.dot(T2_1, Ta2)
T2_a_1 = np.dot(T2_2, Talpha2)
print("\nMatriz de Transformacion T2 -> 1 (TL2): (a2 = {} mm, b2 = {}, tetha2 = {}°, alpha2 = {}°)\n".format(a2, b2, tetha2R, alpha2R), np.matrix(T2_a_1).round(3) )

T3_1 = np.dot(Tb3, Ttetha3)
T3_2 = np.dot(T3_1, Ta3)
T3_a_2 = np.dot(T3_2, Talpha3)
print("\nMatriz de Transformacion T3 -> 2 (TL3): (a3 = {} mm, b3 = {}, tetha3 = {}°, alpha3 = {}°)\n\n".format(a3, b3, tetha3R, alpha3R), np.matrix(T3_a_2).round(3)  )

T10_21 = np.dot(T1_a_0, T2_a_1)
Tfinal = np.dot(T10_21, T3_a_2)
print("\nMatriz de Transformacion T Final (0 -> 3):\n\n", np.matrix(Tfinal).round(3) )






P2 = np.dot(T1_a_0, T2_a_1)
print("\nMatriz de Transformacion Parcial (P2):\n", P2.round(3))

P2_1 = np.dot(Tfinal,  np.linalg.inv(T3_a_2) )
print("\nMatriz de Transformacion Parcial (P2):\n", P2_1.round(3))

P1 = np.dot( P2, np.linalg.inv(T2_a_1) )
print("\nMatriz de Transformacion Parcial 1 (P1):\n", P1.round(3))


print("======== P3 ========")
xJ3 = Tfinal[0,3]
yJ3 = Tfinal[1,3]
print("xJ3:", xJ3.round(3))
print("yJ3:", yJ3.round(3))

print("======== P2 ========")
xJ2 = P2[0,3]
yJ2 = P2[1,3]
print("\nxJ2:", xJ2.round(3))
print("yJ2:", yJ2.round(3))

print("======== P1 ========")
xJ1 = P1[0,3]
yJ1 = P1[1,3]
print("\nxJ1:", xJ1.round(3))
print("yJ1:", xJ1.round(3))


fix, axes = plt.subplots()
plt.plot(0,0,'o')
plt.plot(xJ1, yJ1, 'o')
plt.plot(xJ2, yJ2, 'o')
plt.plot(xJ3, yJ3, 'o')
plt.plot([0,xJ1, xJ2, xJ3], [0,yJ1, yJ2, yJ3])
plt.title("Matrices DH y Transformacion Homegenea Brazo")
plt.xlabel("Posicion X (mm)")
plt.ylabel("Posicion Y (mm)")
plt.show()
