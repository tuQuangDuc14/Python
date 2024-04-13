import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Bieu do duong

#create a array

x = np.linspace(0,10,100)

#su dung object Oriented API
fig, ax=plt.subplots()
ax.plot(x, x**3);
plt.show()