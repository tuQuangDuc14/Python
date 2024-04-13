#Cách sử dụng Try Except
#try:
#đoạn code dự đoná có lỗi
#except:
#hành động khi lỗi xảy ra
#else:
#thực thi code khi khoog có lỗi
#finally: cho phép thucjwj thi



# try:
#     a = int(input("nhap vao so q"))
#     print(a)
# except:
#     print("loi roi ne")


try:
    a = int(input("nhap vao so q"))
    print(a)
except Exception as e:
    print("e")
else:
    print("no e")
finally:
    print("kt")