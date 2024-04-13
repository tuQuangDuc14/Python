#DataFrame

import pandas
import pandas as pd
import numpy as np

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)
print(myvar)

#Tạo DataFrame từ dict các Series 1

s = {
    "Ten": pd.Series(["Duc", "Tho", "Huynh"]),
    "Diem" : pd.Series([10, 9, 8]),
    "Diemrl" : pd.Series([10, 5, 8])
}

st=pd.DataFrame(s)
print(st)

## tạo DataFrame từ dict theo các index được chọn

st1=pd.DataFrame(s, index=[1,0])
print(st1)


# Một số cách thêm cột (column addition)

# thêm cột
st["Mon"]= ["toan", "van", "anh"]
print(st)

st["diemtb"] = (st["Diem"] + st["Diemrl"]) /2
print(st)
# thêm cột True/False theo điều kiện

st["xeploai"] = st["diemtb"] >= 9
print(st)

# xóa cột
del st["Mon"]
print(st)

#Chọn dòng theo label

# chọn dòng theo label no phai la series mới đucợc
# d = s.loc[1]
# print(d)

# Cắt (slice) các dòng
d1=st[1:3] #cắt lấy ra từ dòng 1 đến dòng 2
print(d1)