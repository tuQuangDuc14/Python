emtyList = []

emtyList1 = list()

print(emtyList)
print(emtyList1)

colors =["red", "green", "yellow"]
print(colors)

del(colors[1]) #Xóa phần tử trong list

studentList = ["a", "b", "c"]

listmatch=colors+studentList #Tạo list mới bằng cách nối các list với nhau
listmatch.count("a")         #Đếm số lần xuất hiện của một element trong list
listmatch.index("a")         #Tìm index của element trong list: trả về index nhỏ nhất nếu tìm thấy, nếu không tìm thấy sẽ thông báo lỗi
listmatch.insert(1, "c")     #Chèn một element vào list tại vị trí index

print(studentList[1])
print(studentList[1:2])
studentList.append("d")   #Thêm element vào cuối list
print(studentList)
studentList.insert(2,"e") #them value 
print(studentList)
print(len(studentList))   #len cua list
studentList.remove("e")   #xoa value ra khoi list
print(studentList)

if "a" in studentList: #kiem tra phan tu trong list
    studentList.remove("a")
    print(studentList)


studentList.pop(0) #xoa vi tri
print(studentList)

#dao nguoc list
studentList.reverse()
print(studentList)
studentList = ["a", "c", "v","s"]
#săp xep theo thư tu
studentList.sort()
print(studentList)

numList = [1,2,3,5,8,0]
numList.sort()
print(numList)

#theo thu tu va dao nguoc
numList.sort(reverse=True)
print(numList)

#clear list
numList.clear()
print(numList)

#list chua nhieu dang gia trị khac nhau