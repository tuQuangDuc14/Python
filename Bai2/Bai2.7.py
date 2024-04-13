from MyLib import *

masp=input("nhap mã sản phẩm: ")
tensp=input("nhap tên sp: ")
dongia=input("nhap đơ giá: ")
line=masp+";"+tensp+";"+dongia

savefile("vidu.txt",line)

readf= readfile("vidu.txt")
print(readf)