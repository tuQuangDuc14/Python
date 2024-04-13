#introduction Matpotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[6,7,8,9]

#Chon mau cho do thi
plt.style.available
plt.style.use('seaborn-v0_8-whitegrid')
#ve do thi
plt.plot(x,y, color="blue" );
#show do thi
plt.show()

#cac style trong do thi
# print(plt.style.available)

#sư dung Pylot API va Oject-Oriented API
# Pylot API -> dễ vẽ
#Pylot OO -> nâng cao

