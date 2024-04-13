#Ve sublots 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#optional
# fig, (ax1, ax2), (ax3, ax4) = plt.sublots(nrow=2, ncols=2, figsize=(10,5))

x = np.linspace(0,10,100)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

ax1.plot(x, x*2);
ax1.plot(x, x/2);

ax2.scatter(np.random.random(10), np.random.random(10))

cost_drinks={
    "beer" : 10,
    "milk" : 12,
    "cafe" : 7
}

ax3.bar(cost_drinks.keys(), cost_drinks.values(), color="red")

np.random.seed(42)
students_hieght = np.random.normal(170, 10, 250)
 
ax4.hist(students_hieght, bins=30);
plt.show()