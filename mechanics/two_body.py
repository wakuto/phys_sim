import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

t = np.linspace(0, 50, 1000)
dt = t[1] - t[0]

G = 1
m_1 = 3
m_2 = 4

r_1 = np.zeros((len(t), 2))
r_2 = np.zeros((len(t), 2))

v_1 = np.zeros((len(t), 2))
v_2 = np.zeros((len(t), 2))

a_1 = np.zeros((len(t), 2))
a_2 = np.zeros((len(t), 2))

# mm: 引力を働かせる側の質量
# rr_1: 引力を働かせる側の座標
# rr_2: 引力により力を受ける側の座標
# xx: 計算する引力がx方向なら0, y方向なら1
def grav(mm, rr_1, rr_2, xx):
  distance = np.sqrt(((rr_1[0] - rr_2[0])**2) + ((rr_1[1] - rr_2[1])**2))
  return G*mm*(rr_1[xx] - rr_2[xx])/(distance**3)

# 初期条件
r_1[0, 0] = -0.5
r_1[0, 1] = 0
r_2[0, 0] = 0.5
r_2[0, 1] = 0

v_1[0, 0] = 0
v_1[0, 1] = 1.333
v_2[0, 0] = 0
v_2[0, 1] = -1

a_1[0, 0] = grav(m_2, r_2[0], r_1[0], 0)
a_1[0, 1] = grav(m_2, r_2[0], r_1[0], 1)
a_2[0, 0] = grav(m_1, r_1[0], r_2[0], 0)
a_2[0, 1] = grav(m_1, r_1[0], r_2[0], 1)

def update(i):
  ax.cla()
  ax.set_xlim(-2, 2)
  ax.set_ylim(-2, 2)
  v_1[i] = v_1[i-1] + a_1[i-1]*dt
  v_2[i] = v_2[i-1] + a_2[i-1]*dt

  r_1[i] = r_1[i-1] + v_1[i]*dt
  r_2[i] = r_2[i-1] + v_2[i]*dt

  a_1[i, 0] = grav(m_2, r_2[i], r_1[i], 0)
  a_1[i, 1] = grav(m_2, r_2[i], r_1[i], 1)
  a_2[i, 0] = grav(m_1, r_1[i], r_2[i], 0)
  a_2[i, 1] = grav(m_1, r_1[i], r_2[i], 1)

  ax.scatter([r_1[i-1, 0]], [r_1[i-1, 1]], color="red")
  ax.scatter([r_2[i-1, 0]], [r_2[i-1, 1]], color="blue")

anim = FuncAnimation(fig, update, frames=range(1, len(t)), interval=16)

plt.show()

