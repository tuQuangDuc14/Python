import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Bieu phaan tans

# x = np.linspace(0,10,100)
# plt.scatter(x, np.exp(x))
# plt.show()

#dung OO API
rng=np.random.RandomState(0)

x=rng.randn(100)
y=rng.randn(100)
size = 1000*rng.rand(100)
color = rng.rand(100)
fig, ax = plt.subplots()
color = rng.rand(100)
ab = ax.scatter(x, y, s=size, c=color, cmap="viridis")
fig.colorbar(ab);
plt.show()