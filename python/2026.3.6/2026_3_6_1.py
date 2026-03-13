import math
a=float(input("请输入立方体边长:"))
S=6*pow(a,2)
V=pow(a,3)
print("表面积为:",S,";","体积为:",V)
print("表面积为:%.2f;体积为:%.2f"%(S,V))
print("表面积为:{0:.3f};体积为:{1:.3f}".format(S,V))
print(f"表面积为:{S:.4f};体积为:{V:.4f}")