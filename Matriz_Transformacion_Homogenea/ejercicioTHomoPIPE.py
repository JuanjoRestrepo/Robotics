import numpy as np

b1 = 0
tetha1R = 45
a1 = 200
alpha1R = 0
tetha1 = (tetha1R*np.pi)/180
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

T11 = np.dot(Tb1, Ttetha1)
T21 = np.dot(Ta1, Talpha1)
T1 = np.dot(T11, T21)

print("\nMatriz de Transformacion 1:\n", T1)

#--------------------------------------------------------------------------------

b2 = 0
tetha2R = -45
a2 = 150
alpha2R = 0
tetha2 = (tetha2R*np.pi)/180
alpha2 = (alpha2R*np.pi)/180

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

T21 = np.dot(Tb2, Ttetha2)
T22 = np.dot(Ta2, Talpha2)
T2 = np.dot(T21, T22)

print("\nMatriz de Transformacion 2:\n", T2)

#--------------------------------------------------------------------------------

b3 = 0
tetha3R = -90
a3 = 50
alpha3R = 0
tetha3 = (tetha3R*np.pi)/180
alpha3 = (alpha3R*np.pi)/180

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

T13 = np.dot(Tb3, Ttetha3)
T23 = np.dot(Ta3, Talpha3)
T3 = np.dot(T13, T23)

print("\nMatriz de Transformacion 3:\n", T3)

#--------------------------------------------------------------------------------

Tp = np.dot(T2, T3)
Tf = np.dot(T1, Tp)

print("\nMatriz de Transformacion Final:\n", Tf.round(3))

Tparcial = np.dot(T1, T2)
print("\nMatriz de Transformacion Parcial:\n", Tparcial.round(3))
