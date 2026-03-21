import math
i=0
pi=1
c=0
while i<1000:
    i+=1
    c=(2*i)**2/(2*i-1)/(2*i+1)
    pi*=c
pi=pi*2
print(f"计算结果：{pi}")
print(f"数学库提供的 pi：{math.pi}")