x=float(input("请输入购买金额："))
if x<1000:
    y=x
    print(f"所付钱为：{y:.1f}")
elif 1000<=x<2000:
    y=0.9*x
    print(f"所付钱为：{y:.1f}")
elif 2000<=x<3000:
    y=0.8*x
    print(f"所付钱为：{y:.1f}")
else:
    y=0.7*x
    print(f"所付钱为：{y:.1f}")
