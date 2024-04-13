# kiểu dữ liệu Dictionary
# Từ điển đucợ lưu trữ trữ thành cặp giá trị key:value 
# Từ điển là một tập hợp đucợ sắp xếp theo thứ tự *, có thể thay đổi và không cho phép trung lặp
#Từu điển được sử cặp ngaocwj nhọn

sinhVien = {
    "hovaten" : "Nguyen Van A",
    "malop"   : "10h",
    "diem"    : 10.6
}

print(sinhVien["hovaten"])
print(len(sinhVien))

# su dung get để lấy giá trị
x = sinhVien.get("malop")
print(x)

#thay đổi giá trị
sinhVien["hovaten"] = "11h"
print(sinhVien)

sinhVien.update({"malop":"10j","diem":19})
print(sinhVien)

#them muc moi
sinhVien["noisinh"] = "qung ngai"
print(sinhVien)

sinhVien.update({"tuoi":10,"xeploai":"gioi"})
print(sinhVien)
# xoa
sinhVien.pop("tuoi")
print(sinhVien)

sinhVien.popitem()
print(sinhVien)

del sinhVien["hovaten"]
print(sinhVien)

#duyet

for i in sinhVien.values():
    print(i)

for i in sinhVien.keys():
    print(i)

for i in sinhVien.items():
    print(i)