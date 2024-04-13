a=10
print(type(a))

a="10"
print(type(a))

#####
s1 = "hello"
s2 = "duc"
s3 = s1 + " " + s2 #cong chuoi
print(s3)

cuoi_nhieu_dong = '''
    dong 1
    dong 2
    dong 3
   '''
print(cuoi_nhieu_dong)

chuoi = "My name is Duc\n"
chuoi1 = chuoi*10
print(chuoi1)

#kiem tra chuoi con co thuoc chuoi khac
chuoi_1 = "xin chao duc"
chuoi_2 = "xin"
chuoi_3 = "duc"

if chuoi_2 in chuoi_1:
    print("chuoi 2 yes ")
else:
    print("chuoi 2 no ")

#viet hoa chu dau chuoi
s= "hom nay troi dep qua di mm oi"
s= str.capitalize(s)
print(s)

#viet hoa toan bo chuoi
s=s.upper()
print(s)

#viet thuong toan bo chuoi
s=s.lower()
print(s)

# tim va dem so luong chuoi con
s = "helo everyone hello hello hello"
print(s.find("hello"))
print(s.count("hello"))

# thay the chuoi
s= s.replace("hello","xin chao")
print(s)

# cat chuoi thanh list
list1 = s.split(" ")
print(list1)

print("{0} + {1} = {2}".format(1,2,3))

# lay chuoi con

s = s[1:10]
print(s)

