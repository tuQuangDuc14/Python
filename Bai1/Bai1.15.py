###tupple
## Giá trị của tupple k thể gán giá trị, không thể thay đổi
#tuple không thay đổi, do đó ta không thể cập nhật/ xóa phần tử trong tuple
#Chỉ có thể xóa bỏ cả tuble
#Cũng tương tự như các phương thức cơ bản của list nhưng không có phương thức: 
#sort, reverse, remove, pop, insert, extend, append


gioiTinh = ("Nam", "Nu")
lopHoc = (1,2,3,4,5,6,7)
traiCay = ("Tao","Man","Oi","Tao","Xoai")

print(gioiTinh[0])
# gioiTinh[0] ="namq"
del(traiCay)
for x in traiCay:
    print(x)

y=(1,2,3) + (4,5,6) 
# cong hai tupple
print(y)

y=(1,2,3)*2
print(y)
# tra ve true hay false
print("mit" in traiCay)
# len
z = len(traiCay)
print(z)

print(traiCay.count("Tao"))
# tim min max
print(min(lopHoc))
print(max(lopHoc))
print(sum(lopHoc))

listCay= sorted(traiCay)
print(listCay)

listCay= sorted(lopHoc)
print(lopHoc)