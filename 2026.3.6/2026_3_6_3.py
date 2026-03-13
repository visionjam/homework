import math
a,b,C=eval(input("输入边长a,边长b,夹角角度:"))
C=C*math.pi/180
C1=math.cos(C)
c=math.sqrt(a**2+b**2-2*a*b*C1)
print(f"边长c:{c:.2f}")