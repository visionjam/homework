import math
angle=float(input("请输入角度:"))
x=float(input("请输入浮点数值x："))
radian=math.pi/180*angle
sin1=math.sin(radian)
log1=math.log((math.fabs(x))+1)
sqrt1=math.sqrt(x*x+1)
a=sin1+log1-sqrt1
print("表达式结果:",a)