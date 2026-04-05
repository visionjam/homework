n=eval(input("请输入n:"))
fib=[0,1,1,2]
def f(n):
    if n==0 or n==1:
        return 0
    elif n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
print(f"第{n}项是{f(n)}")