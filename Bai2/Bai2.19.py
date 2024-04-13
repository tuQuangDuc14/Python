import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#bieeur ddoof cootj

# vertical and Horizontal

cost_drinks={
    "beer" : 10,
    "milk" : 12,
    "cafe" : 7
}

fig, ax = plt.subplots()
ax.bar(cost_drinks.keys(), cost_drinks.values(), color="red")
ax.set(title="Loai do uong", ylabel="Cost")
plt.show()