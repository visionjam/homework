n=int(input("请输入n: "))
a=[0,1]
b=[0,1]

def fib(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        b=fib(n-1)
        b.append(b[-1]+b[-2])
        return b

if n <=0:
    a=[]
    print(a)
elif n==1 :
    a=[0]
    print(a)
elif n==2 :
    a=[0,1]
    print
else:
    b=fib(n)
    print(b)