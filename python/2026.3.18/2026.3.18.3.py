a=input("请输入表达式：")
zuo=0
you=0
for i in a:
    if i =="(":
        zuo+=1
    elif i ==")":
        you+=1
if zuo>you:
    print("左括号多于右括号")
elif zuo<you:
    print("右括号多于左括号")
else:
    print("圆括号配对正确")
