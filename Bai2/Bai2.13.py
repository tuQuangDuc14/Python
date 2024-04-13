import pandas as pd

df = pd.read_excel(r'Book1.xlsx')

print(df.to_string()) 

#dem so hang so cot
print(df.shape)

#in mot cot
c2=pd.DataFrame(df, columns=['Ten'])
print(c2)


print(df.info())
print(df.describe())

# loc ra cai can
df.loc[df.Diem == 10]
print(df.loc[df.Diem == 10])

#loc hang
print(df.iloc[2])

# thêm cột
df["Mon"]= ["toan", "van", "anh", "sinh", "lsu"]
print(df)

x = (df["Diem"].sum())/3
print(x)

mx=df.groupby("Diem").apply(print)

#sap xep
print(df.Diem.value_counts())