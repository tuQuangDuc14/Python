#vong lap for
tong=0
for i in range(10):
    tong +=i
    print(tong)
print(tong)
#########

for i in range(0,18,2):
    print(i)

#######
for i in range(18,0,-2):
    print(i)

colors=["red","green","yelow"]
##Vong for trong list
for i in colors:
    print(i)

#Duyet vong for theo vi tri
for i in range(len(colors)):
    print(colors[i])

##in bang cua chuong
for i in range(1,11):
    print("2 x {0} = {1}".format(i,2*i))

########
for i in range(2,10):
    print("bang cua chuong", i)
    for j in range(1,11):
        print("{0} x {1} = {2}".format(i,j,j*i))