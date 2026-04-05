def fac(d,r):
    q=d//r
    l=d%r
    if q==0:
        return str(d)
    elif q!=0:
        return fac(q,r) + str(l)


print(f"10的2进制：{fac(10,2)}")
print(f"25的8进制：{fac(25,8)}")
print(f"20的5进制：{fac(20,5)}")
print(f"123的9进制：{fac(123,9)}")

