# kiểu dũ liệu Set trong python
# Set là tập hợp không có thứ tự, giá trị không đucợ trùng nhsu, không thể thsy đổi * và không lập chỉ mục . Lưu ý mục set là không thể thay đổi 
# nhưng bạn có thể xóa các mục và thêm các mục mới
# sử dụng cặp ngoặc {}
monHoc = {"Toan","Ly","Hoa"}
print(monHoc)

for i in monHoc:
    print(i)

# sử dung add thêm phần tử
monHoc.add("Anh")
print(monHoc)
# giá trị  trùng nhau thì nó sẽ ghi đè
monHoc.add("Anh")
print(monHoc)

# thêm nhiều phần tử
hocThem = {"Su", "cong dan"}
monHoc.update(hocThem)
print(monHoc)

#thêm 1 list vào 1 set
hocPhudao= ["Vo","Tin","Li"]
monHoc.update(hocPhudao)
print(monHoc)

# xoa phan tu trong set 
# xoa đi phần tử in set nếu mà k tồn tại phần tử thì sẽ phát sinh lôi
monHoc.remove("Anh") 
print(monHoc)
# xoa đi phần tử in set nếu mà k tồn tại phần tử thì sẽ k phát sinh lôi
monHoc.discard("Su")
print(monHoc)

monHoc.pop() #lấy ra phần tử đầu tiên
print(monHoc)

monHoc.clear() #xoa het
print(monHoc)

del monHoc
print(monHoc)
