def fx(x):
    f=2*x**3-4*x**2+3*x-6
    return f

def root(a,b):
    fa=fx(a)
    fb=fx(b)
    while (abs(a-b)>1e-6):
        m=(a+b)/2
        fm=fx(m)
        if(fa*fm>0):
            a=m
        elif (fa*fm<0):
            b=m
        else:
            return m
    return (a+b)/2

a=-10
b=10
print(f"方程在区间[-10,10]内的根为：{root(a,b):.6f}")