#输入系数
a=float(input("请输入系数a:"))
b=float(input("请输入系数b:"))
c=float(input("请输入系数c:"))

import math
d=b**2-4*a*c

if d<0:
    print("该方程无实数根")
else:
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)

    if d==0:
        print(f"重根，即相同得根:x1=x2={root1:.2f}")
    else:
        print(f"该方程有两个实根:x1={root1:.2f},x2={root2:.2f}")