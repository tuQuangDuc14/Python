#bieu do the hien tan suat

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
students_hieght = np.random.normal(170, 10, 250)

plt.hist(students_hieght, bins=30);
plt.show()