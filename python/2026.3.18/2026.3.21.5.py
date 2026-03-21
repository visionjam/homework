x=int(input("请输入一个正整数："))
nx=0
if x<=0:
    print("输入的数字必须为正整数!")

else: 
    while x != 0:
            x1=x%10
            x=x//10
            nx=10*nx+x1
    print("逆序数为：",nx)
