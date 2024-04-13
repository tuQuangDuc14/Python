# #dem chu cai
# def Demchucai(*content):
#     Dis={}
#     for L in content:
#         for Li in L:
#             Li=Li.upper()
#             if(Li in Dis):
#                 Dis[Li]+=1
#             else:
#                 Dis[Li]=1
#     return Dis
# dem = Demchucai("kk","123","ffhfh")
# print(dem)
import datetime

class Student:
    def __init__(self, name, age):
        print("Name is ",name, "age", age)
    def __str__(self):
        return ("fhfhhfhf")

Duc=Student("duc",23)
print(Duc)



x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A")) #thu may trong tuan

x = datetime.datetime(2020, 5, 17)

print(x)

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B")) #thang may 