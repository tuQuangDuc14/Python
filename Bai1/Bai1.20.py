#hàm trong funtion
def xinchao():
    print("xin chao")

xinchao()

def Ten(Hovaten):
    print("toi ten la " + Hovaten)

Ten("Duc")

#khi không xác định đucợ số đối số, chungsta có thể sử dụng dáu *

def ThoiKhoaBieu(*monhoc):
    print(monhoc[0])
    print(monhoc[1])
    print(monhoc[3])
    print(*monhoc)

ThoiKhoaBieu("toan","ton","tn","oan","ta",)

def sum(*value):
    summ=0
    for x in value:
        summ=summ+x
        print(x)
    print(summ)

sum(2,4,5,6)

#truyền nhieuf đối số xác định qa tên, sử dụng **

#sử dụng return
def tinh(*giatri):
    tich=1
    for x in giatri:
        tich=tich*x
    return tich

z=tinh(2,4)
t=tinh(2,4,1)
print(z)
print(t)

def gcd(a,b):
    while(a!=b):
        if a>b:
            a=a-b
        else:
            b=b=a
    return a

ucnn=gcd(111,300)
print(ucnn)

list_num=[]
n=1
try:
    n = int (input("nhap vo n:"))
except:
    n=1

def Nhap(n,list_num):
    for i in range(n):
        list_num.append(int(input("nhap value")))

def tong(list_num):
    x=0
    for i in list_num:
        x=x+i
    return x

Nhap(n,list_num)
o=tong(list_num)
print(o)