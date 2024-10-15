import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)

g = 9.81
m = 1
k = 0.1

# 速度の計算
v_x = 10
v_y = 20

v = [np.array([v_x, v_y])]

for i in range(1, len(t)):
  dv_x = (-k/m * v[i-1][0]) * (t[i] - t[i-1])
  dv_y = (-k/m * v[i-1][1] - g) * (t[i] - t[i-1])

  v_x += dv_x
  v_y += dv_y
  v.append(np.array([v_x, v_y]))

v = np.array(v)

# 位置の計算
x = 0
y = 0

r = [np.array([x, y])]

for i in range(1, len(t)):
  x += v[i, 0] * (t[i] - t[i-1])
  y += v[i, 1] * (t[i] - t[i-1])
  r.append(np.array([x, y]))

r = np.array(r)

plt.scatter(r[:, 0], r[:, 1])
plt.show()

