def f(x):
    a=int(str(x)[-3])
    b=int(str(x)[-2])
    c=int(str(x)[-1])
    return a**3+b**3+c**3
d=[]
for i in range(100,1000):
    if i==f(i):
        d+=[i]
print(d)