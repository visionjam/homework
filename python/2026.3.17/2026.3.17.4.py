a=float(input("请输入上网时间（小时）："))
if a<10:
    print("上网费用:30元")
elif 10<=a<=50:
    b=30+2.5*(a-10)
    print(f"上网费用:{b}元")
else:
    b=30+40*2.5+2*(a-50)

    if b<=150:
        print(f"上网费用:{b}元")

    else:
        print("上网费用:150元")

    