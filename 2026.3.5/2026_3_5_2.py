a=float(input("请输入矩形的长:"))
b=float(input("请输入矩形的宽:"))
if a>0 and b>0:

    if a == b:
        print("这是一个正方形")
    else:
        print("这是一个长方形")
    s=(a*b)
    c=(2*a+2*b)
    print("面积s=",s)
    print("周长c=",c)
else:
    print("请输入两边边长都大于0的数值！")