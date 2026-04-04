def fun(x):
    return int(str(x)[::-1])
a=[]
for i in range(1000,10000):
    if i == fun(i):
        print(i,end=" ")