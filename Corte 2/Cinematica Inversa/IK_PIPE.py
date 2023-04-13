import numpy as np
import matplotlib.pyplot as plt
'''
xp = float(input("Ingresa la coordanada X: "))
yp = float(input("Ingresa la coordanada Y: "))
zp = float(input("Ingresa la coordanada Z: "))
a2 = float(input("Ingresa la longitud del eslabon 2: "))
a3 = float(input("Ingresa la longitud del eslabon 3: "))
b1 = float(input("Ingresa el parametro b de la matriz DH: "))
'''
xp = 297.972
yp = 297.972
zp = 328.341
a1 = 150
a2 = 250
a3 = 232
b1 = 300

p1x = np.sqrt((xp**2)+(yp**2))

tetha1 = np.arctan(yp/xp)

num1 = -(zp**2)-(p1x**2)+(a2**2)+(a3**2)
den1 = 2*a2*a3
tetha3 = np.arccos(num1/den1)-np.pi

num2 = -(zp**2)-(p1x**2)-(a2**2)+(a3**2)
den2 = -2*a2*(np.sqrt((p1x**2)+(zp**2)))
tetha2 = (np.arccos(num2/den2))+(np.arctan(zp/p1x))

teta1p = (tetha1*180)/np.pi
teta2p = (tetha2*180)/np.pi
teta3p = (tetha3*180)/np.pi

print("tetha1 = ", teta1p)
print("tetha2 = ", teta2p)
print("tetha3 = ", teta3p)

#--------------------------------------------------------------------------------

a1 = 150    # 0 -> ORIGINAL PIPE
alpha1R = 0     # 90 -> ORIGINAL PIPE
alpha1 = (alpha1R*np.pi)/180

Tb1 = [[1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, b1],
      [0, 0, 0, 1]]

Ttetha1 = [[np.cos(tetha1), -np.sin(tetha1), 0, 0],
          [np.sin(tetha1), np.cos(tetha1), 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]]

Ta1 = [[1, 0, 0, a1],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]

Talpha1 = [[1, 0, 0, 0],
         [0, np.cos(alpha1), -np.sin(alpha1), 0],
          [0, np.sin(alpha1), np.cos(alpha1), 0],
          [0, 0, 0, 1]]

T11 = np.matmul(Tb1, Ttetha1)
T21 = np.matmul(Ta1, Talpha1)
T1 = np.matmul(T11, T21)

print("\nMatriz de Transformacion 1:\n", T1)

#--------------------------------------------------------------------------------

b2 = 0
alpha2 = 0

Tb2 = [[1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, b2],
      [0, 0, 0, 1]]

Ttetha2 = [[np.cos(tetha2), -np.sin(tetha2), 0, 0],
          [np.sin(tetha2), np.cos(tetha2), 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]]

Ta2 = [[1, 0, 0, a2],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]

Talpha2 = [[1, 0, 0, 0],
         [0, np.cos(alpha2), -np.sin(alpha2), 0],
          [0, np.sin(alpha2), np.cos(alpha2), 0],
          [0, 0, 0, 1]]

T21 = np.matmul(Tb2, Ttetha2)
T22 = np.matmul(Ta2, Talpha2)
T2 = np.matmul(T21, T22)

print("\nMatriz de Transformacion 2:\n", T2)

#--------------------------------------------------------------------------------

b3 = 0
alpha3 = 0
Tb3 = [[1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, b3],
      [0, 0, 0, 1]]

Ttetha3 = [[np.cos(tetha3), -np.sin(tetha3), 0, 0],
          [np.sin(tetha3), np.cos(tetha3), 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]]

Ta3 = [[1, 0, 0, a3],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]

Talpha3 = [[1, 0, 0, 0],
         [0, np.cos(alpha3), -np.sin(alpha3), 0],
          [0, np.sin(alpha3), np.cos(alpha3), 0],
          [0, 0, 0, 1]]

T13 = np.matmul(Tb3, Ttetha3)
T23 = np.matmul(Ta3, Talpha3)
T3 = np.matmul(T13, T23)

print("\nMatriz de Transformacion 3:\n", T3)

#--------------------------------------------------------------------------------

Tp = np.matmul(T2, T3)
Tf = np.matmul(T1, Tp)

print("\nMatriz de Transformacion Final:\n", Tf)

p1f = np.matmul(T1, [[0], [0], [0], [1]])
p2a = np.matmul(T2, [[0], [0], [0], [1]])
p2f = np.matmul(T1, p2a)
p3a = np.matmul(T3, [[0], [0], [0], [1]])
p3b = np.matmul(T2, p3a)
p3f = np.matmul(T1, p3b)
print(p1f)
print(p2f)
print(p3f)

fix, axes = plt.subplots()
plt.plot(0,0,'o')
plt.plot(p1f[0,0], p1f[1,0], 'o')
plt.plot(p2f[0,0], p2f[1,0], 'o')
plt.plot(p3f[0,0], p3f[1,0], 'o')
plt.plot([0, p1f[0,0], p2f[0,0], p3f[0,0]], [0, p1f[2,0], p2f[2,0], p3f[2,0]])
plt.title("Matrices DH y Transformacion Homegenea Brazo")
plt.xlabel("Posicion X (mm)")
plt.ylabel("Posicion Z (mm)")
plt.show()
