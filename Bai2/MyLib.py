def Sum(*data):
    s=0
    for i in data:
        s+=i
    return s
def Tich(*data):
    s=1
    for i in data:
        s*=i
    return s

def savefile(path,data):
    fili = open(path,'a',encoding='utf-8')
    fili.writelines(data)
    fili.writelines("\n")
    fili.close()

def readfile(path):
    arr=[]
    fili = open(path,'r',encoding="utf-8")
    for line in fili:
        data=line.strip()
        print(data)
        arrr=data.split(";")
        arr.append(arrr)
    fili.close()
    return arr
