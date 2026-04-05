x=float(input("请输入x(0~3.14之间):"))
import math
sin=math.sin(x)
s=0
sign=1
power=1

def fac(a):
    if a== 0 or a== 1:
        return 1
    else:
        return a*fac(a-1)
    
n=(x**power)*sign/(fac(power))
while abs(n)>=1e-6:
    sign=-sign
    power+=2
    s+=n
    n=(x**power)*sign/(fac(power))

print(f"x = {x} 时，级数和为 {s}")
print(f"math.sin({x}) 的值为 {sin}")