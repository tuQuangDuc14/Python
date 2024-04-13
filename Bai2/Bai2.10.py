import pandas
import pandas as pd
import numpy as np
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pandas.DataFrame(mydataset)

# đay là series

#khong truyen index
a = [1, 7, 2, 6, 9]

myvar = pd.Series(a)

print(myvar)
print(myvar[0])

#truyen index
s = pd.Series([0,1,2,3], index=["a","b","c","d"])
print(s)

#Tạo Series từ dict
dir={
   'a': 1,
   'b': 21,
   'd': 11,
   'f': 12,
}

st=pd.Series(dir, index=['a','b','d','f'])
print(st)
print(st['f'])
print(st['b':'f'])
#Tạo Series từ Scalar

ser = pd.Series(a, index=[1, 2, 3, 4, 5])
print(ser)