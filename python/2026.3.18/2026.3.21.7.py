a=int(input("请输入 a（1~9）："))
n=int(input("请输入 n（5~10）："))

temp=0
ss=""
count=0
for i in range(1,n+1):
    temp=temp*10+a
    ss+=str(temp)+"+"
ss=ss[:-1]
for s in ss.split("+"):
    count+=int(s)
print(f"Sn={ss}={count}")