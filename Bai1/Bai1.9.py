from math import sqrt

xA = float(input("nhap vao xA"))
yA = float(input("nhap vao yA"))

xB = float(input("nhap vao xB"))
yB = float(input("nhap vao yB"))

xC = float(input("nhap vao xC"))
yC = float(input("nhap vao yC"))

ab = sqrt((xB-xA)**2 + (yB - yA)**2)
bc = sqrt((xC-xB)**2 + (yC - yB)**2)
ac = sqrt((xC-xA)**2 + (yC - yA)**2)

if (ab + bc > ac) and (ab+ac > bc) and (bc+ac > ab):
    print("hhhaha")

else:
    print("jjjjj")


if (ab +c) and (ab-s) or 