import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#su dụng API
x = np.linspace(0, 10, 1000)
plt.style.available
plt.style.use('seaborn-v0_8-whitegrid')
plt.plot(x, np.sin(x), color="red", linestyle="dashed", label="sin(x)");
#hai do thi tren cung plot
plt.plot(x, np.cos(x), color="green", label="cos(x)");
#đat tên cho các truc toa độ
plt.xlabel("BienX")
plt.ylabel("SinX")
#giơi hạn độ dai độ thị có thì dùng hàm axis(xmin, xmax, ymin, ymax)
# plt.xlim([0,4])
# plt.ylim([0,0.75])

#Khi tạo leble cho các đồ thi, cần call hàm 
plt.legend()

#đat tên cho đồ thi
plt.title("Đồ thị Sin Cos")
plt.show()