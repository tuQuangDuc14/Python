output_file = "output.txt"
content1 = "Nội dung đoạn 1 cần ghi vào tệp." 
content2 = "Nội dung đoạn 2 cần ghi vào tệp." 
with open(output_file, 'a', encoding='utf-8') as file:    
    file.write(content1)    
    file.write('\n')    
    file.write(content2)    
    file.write('\n')
print("Đã ghi nội dung vào tệp.")