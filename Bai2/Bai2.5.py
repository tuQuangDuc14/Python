#open
#"x"
try:
    f=open("vidu.txt", "x")

except Exception as e:
    print(e)
#"w" ghi du lieu file
#"a" noi file
try:
    with open("vidu.txt", "a") as f:
        f.write("xin chao mn\n")
        f.close()
except Exception as e:
    print(e)
#"r" doc du lieu file
try:
    with open("vidu.txt", "r") as f:
        noidung = f.read()
        print(noidung)
except Exception as e:
    print(e)
