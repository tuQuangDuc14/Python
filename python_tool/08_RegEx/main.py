import re

# # []: tập các ký tự bạn muốn khớp
# # pattern = '[a-e]'
# # test_string = 'abcde'

# # Nếu ký tự đầu tiên của tập hợp là ^ thì tất cả các ký tự không được định nghĩa trong tập hợp sẽ được so khớp.
# # pattern = '[^abc]'
# # test_string = 'de'

# # . Dấu chấm khớp với bất kỳ ký tự đơn thông thường nào ngoại trừ ký tự tạo dòng mới '\n'.
# # so luong ki tu trog chuoi
# # pattern = '..'
# # test_string = 'dn'

# # # Biểu tượng dấu mũ ^ được sử dụng để khớp ký tự đứng đầu một chuỗi.
# # pattern = '^a'
# # test_string = 'adn'

# # # Biểu tượng Dollar $ được sử dụng để khớp ký tự kết thúc một chuỗi.
# # pattern = 'a$'
# # test_string = 'a'

# # # Biểu tượng dấu hoa thị * có thể khớp với chuỗi có hoặc không có ký tự được định nghĩa trước nó. Ký tự này có thể được lặp lại nhiều lần mà không bị giới hạn số lượng.
# # pattern = 'ma*n'
# # test_string = 'mn'

# # # Biểu tượng dấu cộng + có thể khớp với chuỗi có một hoặc nhiều ký tự được định nghĩa trước nó. Ký tự này có thể được lặp lại nhiều lần mà không bị giới hạn số lượng.
# # pattern = 'ma+n'
# # test_string = 'maaaaan'

# # # Biểu tượng dấu chấm hỏi có thể khớp với chuỗi có hoặc không có ký tự được định nghĩa trước nó. Ký tự này không thể được lặp lại nhiều lần, chỉ giới hạn số lượng với một lần xuất hiện.
# # pattern = 'ma?n'
# # test_string = 'man'

# # # {n,m}, đại diện cho việc ký tự đằng trước nó có thể xuất hiện tối thiểu n lần vào tối đa m lần. n và m là số nguyên dương và n <= m.
# # pattern = 'a{2,3}'
# # test_string = 'aabc daaaat'

# # # Biểu tượng dấu sổ dọc | này có thể khớp với chuỗi tồn tại 1 trong 2 ký tự được định nghĩa trước và sau nó.
# # pattern = 'a|b'
# # test_string = 'aabc daaaat'

# # Dấu ngoặc đơn () được sử dụng để gom nhóm các pattern lại với nhau, chuỗi sẽ khớp với biểu thức chính quy bên trong dấu ngoặc này.
# pattern = '(a|b|c)xz'
# test_string = 'axz'
# # re.match() để tìm kiếm test_string tương ứng với pattern.
# result = re.match(pattern, test_string)

# if result:
#   print("Tim kiem thanh cong.")
# else:
#   print("Tim kiem khong thanh cong.")


# # Pattern ta hiểu là một đối tượng mẫu, một phiên bản đã được biên dịch của một biểu thức chính quy. 
# # Để chỉ định biểu thức chính quy, ta sử dụng các ký tự đặc biệt, bao gồm:
# # [] . ^ $ * + ? {} () \ |

# # Regular Expression trong Python

# # re.findall() trả về một danh sách các chuỗi chứa tất cả các kết quả khớp với pattern đưa ra.
# string = 'hello 12 hi 89. Howdy 34'
# pattern = '\d+'

# result = re.findall(pattern, string) 
# print(result)

# # Phương thức re.split() dùng biểu thức chính quy để ngắt chuỗi thành các chuỗi con và trả về danh sách các chuỗi con này.
# string = 'The rain in Vietnam.'
# pattern = '\s'

# result = re.split(pattern, string) 
# print(result)

# string = 'The rain in Vietnam.'
# pattern = '\s'

# result = re.split(pattern, string, 1) 
# print(result)

# # Re.sub() sẽ thay thế tất cả các kết quả khớp với pattern trong chuỗi bằng một nội dung khác được truyền vào và trả về chuỗi đã được sửa đổi.
# # chuỗi nhiều dòng
# string = 'abc 12\
# de 23 \n f45 6'

# # so khớp các ký tự khoảng trắng
# pattern = '\s'

# # chuỗi rỗng
# replace = ''

# new_string = re.sub(pattern, replace, string) 
# print(new_string)

# # Phương thức re.search() sử dụng để tìm kiếm chuỗi phù hợp với pattern RegEx. Nếu tìm kiếm thành công, re.search() trả về đối tượng khớp, nếu không, nó trả về None.
# string = "Quantrimang.com la website ban co the hoc Python"

# # Kiem tra xem 'Quantrimang' co nam o dau chuoi khong
# match = re.search('\AQuantrimang', string)

# if match: # nếu tồn tại chuỗi khớp
#   print("Tim thay 'Quantrimang' nam o dau chuoi") # in ra thong bao nay
# else:
#     print("'Quantrimang' khong nam o dau chuoi") # khong thi in ra thong bao nay

# string = '39801 356, 2102 1111'

# pattern = '(\d{3}) (\d{2})'

# match = re.search(pattern, string)

# if match: #nếu tồn tại chuỗi khớp
#   print(match.group()) # in ra kết quả
# else:
#   print("Không khớp") # Không thì hiện thông báo

# # Sử dụng tiền tố r trước RegEx
pattern = r'\BThe'
test_string = 'vvThehekko'
# re.match() để tìm kiếm test_string tương ứng với pattern.
result = re.match(pattern, test_string)

if result:
  print("Tim kiem thanh cong.")
else:
  print("Tim kiem khong thanh cong.")
