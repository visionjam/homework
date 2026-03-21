s=0
s1=1
c=0
while s1>=1e-4:
    c+=1
    t1=(c**2-c+2)/2
    s1=1/(t1)
    if s1<1e-4:
        break
    s+=s1

print("s=",s,end="")
print()
print(f"计算了{c-1}项")