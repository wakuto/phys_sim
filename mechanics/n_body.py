import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

t = np.linspace(0, 10, 500)
dt = t[1] - t[0]

G = 5
# m = np.array([1, 1, 1])
m = np.ones(20)
m[-1] = 1000

r = np.zeros((len(m), len(t), 2))
v = np.zeros((len(m), len(t), 2))
a = np.zeros((len(m), len(t), 2))

# mm: 引力を働かせる側の質量
# rr_1: 引力を働かせる側の座標
# rr_2: 引力により力を受ける側の座標
# xx: 計算する引力がx方向なら0, y方向なら1
def grav(mm, rr_1, rr_2, xx):
  distance = np.sqrt(((rr_1[0] - rr_2[0])**2) + ((rr_1[1] - rr_2[1])**2))
  return G*mm*(rr_1[xx] - rr_2[xx])/(distance**3)

# 初期条件
rng = np.random.default_rng()
for i in range(len(m)-1):
  rad = 10 + rng.standard_normal()*2
  theta = rng.standard_normal() * np.pi
  r[i][0, 0] = rad * np.cos(rad)
  r[i][0, 1] = rad * np.sin(rad)
  vel = 20#(1 + rng.standard_normal())*5
  v[i][0, 0] = -vel * np.sin(rad)
  v[i][0, 1] = vel * np.cos(rad)

# r[0][0, 0] = 0
# r[0][0, 1] = 0
# r[1][0, 0] = 1
# r[1][0, 1] = 0
# r[2][0, 0] = 0.5
# r[2][0, 1] = 0.5*3**0.5

# v[0][0, 0] = 0
# v[0][0, 1] = 1
# v[1][0, 0] = 0
# v[1][0, 1] = -1
# v[2][0, 0] = -1
# v[2][0, 1] = 0

for j in range(len(m)):
  a[j][0, 0] = 0
  a[j][0, 1] = 0
  for k in range(len(m)):
    if j != k:
      a[j][0, 0] += grav(m[k], r[k][0], r[j][0], 0)
      a[j][0, 1] += grav(m[k], r[k][0], r[j][0], 1)

def update(i):
  ax.cla()
  ax.set_xlim(-20, 20)
  ax.set_ylim(-20, 20)

  # t=i 時点での、j番目の粒子の速度・位置を計算
  for j in range(len(m)):
    v[j][i] = v[j][i-1] + a[j][i-1]*dt
    r[j][i] = r[j][i-1] + v[j][i]*dt


  # t=i のとき、j番目の粒子がk番目の粒子から受ける力を調べる
  for j in range(len(m)):
    a[j][i, 0] = 0
    a[j][i, 1] = 0
    for k in range(len(m)):
      if j != k:
        # print(f'{i*dt:.3f}, {j}, {k}')
        a[j][i, 0] += grav(m[k], r[k][i], r[j][i], 0)
        a[j][i, 1] += grav(m[k], r[k][i], r[j][i], 1)

  for j in range(len(m)):
    ax.scatter([r[j][i-1, 0]], [r[j][i-1, 1]])
    ax.plot(r[j][max(0, i-50):i, 0], r[j][max(0, i-50):i, 1])


anim = FuncAnimation(fig, update, frames=range(1, len(t)), interval=16)

plt.show()
anim.save("n-body4.gif", writer="imagemagick")

