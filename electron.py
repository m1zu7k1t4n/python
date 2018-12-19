#%%
import math
import numpy as np
import matplotlib.pyplot as plt

pi = math.pi  # mathモジュールのπを利用
E = 10
C = 0.001
R = 100+
t = np.linspace(0, 10, 100000)  # 0から2πまでの範囲を100分割したnumpy配列
# v0 = E*(1-np.exp(-t/(R*C)))
i0 = (E/2)*(np.exp(-2*t) - np.exp(-10*t))
i1 = (2/3)*E*np.exp(-t)*np.sin(3*t)
hou = (2/3)*E*np.exp(-t)
houm = -(2 / 3) * E * np.exp(-t)

# plt.plot(t, v0)
plt.plot(t, i0)
plt.plot(t, i1)
plt.plot(t, hou,linestyle="dotted",color="black")
plt.plot(t, houm,linestyle="dotted", color="black")
plt.grid()
# plt.sticks([-1,0,1])
plt.show()
