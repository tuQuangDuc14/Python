import random

# khai bao 1 cái set
thungPhieu = set()

while(True):
    print("----------MENU------------")
    print("Vui long nhap chuc nang: ")
    print("1 - Thêm số điện thoại cuả bạn vào thùng phiếu")
    print("2 - Xóa một số điện trong thùng phiếu")
    print("3 - Quay số trúng thuong")
    print("4 - Kết thúc chương trình")
    print(thungPhieu)
    print("----------MENU------------")
    luaChon = int(input("Lua chon: "))
    if(luaChon == 1):
        sodienthoai = input("nhap so dien thoai của ban")
        thungPhieu.add(sodienthoai)
    elif (luaChon ==2):
        sodienthoai = input("nhap so dien thoai can xoa")
        thungPhieu.discard(sodienthoai)
    elif (luaChon ==3):
        index=random.randint(0,len(thungPhieu)-1)
        print("vi tri trung thuong"+str(index))

        i=0
        for x in thungPhieu:
            if(i==index):
                break
            i=i+1
        print("chuc mung so dien thoai: "+ x + "đã trung thương")
    else:
        break

    input("Nhap tiếp tục")