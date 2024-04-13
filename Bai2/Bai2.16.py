#su dung object Oriented API
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#chuẩn bị data

x=[1,2,3,4]
y=[5,7,9,12]

#2 Setup plot
fig, ax = plt.subplots(figsize=(5,5)) #figure size = width, hieght

#3 plot the data

ax.plot(x,y)

ax.set(title="Do thi oject", xlabel="x", ylabel="y")

plt.show()

#most common types of Matplotlib plots
# line
# scatter
# bar
# hist
# subplots()

