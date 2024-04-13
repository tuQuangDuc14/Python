import numpy as np

#Khởi tạo mảng một chiều với kiểu dữ liệu các phần tử là Integer
a=[1,3,4,5,6]
arr= np.array(a,dtype = int)
print(arr)
print(arr[1])
print(arr[2] + arr[3])
print(arr[1:3])
print(arr[1:4:2])
# Make a copy, change the original array, and display both arrays:
x = arr.copy()
print(x)
x = arr.view()
print(x)
print("Kích thước của mảng:", arr.shape)
print("Số phần tử trong mảng:", arr.size)
print("Số chiều của mảng:", arr.ndim)
print("Kiểu dữ liệu của phần tử trong mảng:", arr.dtype)
# Khởi tạo mảng hai chiều
a1= [(1,2,3), (4,5,6)]
arr1 = np.array(a1)
#Khởi tạo với các hàm có sẵn
#Tạo mảng hai chiều các phần tử 0 với kích thước 3x4.
arr2= np.zeros((3,4), dtype = int)
print(arr2)

#Tạo mảng 3 chiều các phần tử 1 với kích thước 2x3x4.
arr3=np.ones((2,3,4), dtype = int)
print(arr3)

# Tạo mảng với các phần tử từ 1 - 6 với bước nhảy là 2.
arr4=np.arange(1,7,2)
print(arr4)

#Tạo mảng 2 chiều các phần tử 5 với kích thước 2x3.
arr5=np.full((2,3),5)
print(arr5)

#np.eye(4, dtype=int): Tạo ma trận đơn vị với kích thước là 4x4.
arr6=np.eye(4, dtype=int)
print(arr6)

#np.random.random((2,3)): Tạo ma trận các phần tử ngẫu nhiên với kích thước 2x3.

diem=np.loadtxt('vidu.txt', dtype=int, delimiter=',')
print("File dữ liệu điểm lớp 2A:\n", diem)

print("Giá trị lớn nhất của mảng arr là:", np.max(diem))
print("Giá trị trung vị của mảng arr là:", np.median(diem))
print("Giá trị nhỏ nhất của mảng arr là:", np.min(diem))
print("Tổng tất cả các phần tử của mảng arr là:", np.sum(diem))
print("Trung bình cộng tất cả các phần tử của mảng arr là:", np.mean(diem))

a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)

# # đôi cột trành dòng
# b=np.arange(20).reshape(4,5)
# print(b)
# print(b.T)

# c=a.copy()
# print(c)
print(a.T)
print(a.shape[0]) #so hang
print(a.shape[1]) #so cot
b=a.reshape((a.shape[1]),(a.shape[0]))
print(b)
print(b.T)
# ar2=np.zeros((a.shape[1], a.shape[0]))
# print(ar2)

# dem = 0
# for row in a:
#     ar2[:dem] = row
#     dem = dem +1

# print(ar2)
