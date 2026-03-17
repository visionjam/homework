x=int(input("请输入第一个数字:"))
y=int(input("请输入第二个数字:"))
z=int(input("请输入第三个数字:"))


if x<y:
    if y<z:
        x,z=z,x
        print(f"{z}<{y}<{x}")
    elif y==z:
        print(f"{z}={y}<{x}")
    elif y>z:
        if x>z:
            print(f"{z}<{x}<{y}")
        elif x<z:
            print(f"{x}<{z}<{y}")
        else:
            print(f"{z}={x}<{y}")

elif x==y:
    if y<z:
        print(f"{x}={y}<{z}")
    elif y==z:
        print(f"{z}={y}={x}")
    else:
        print(f"{z}<{y}={x}")

else:
    if y>z:
        print(f"{z}<{y}<{x}")
    elif y==z:
        print(f"{z}={y}<{x}")
    else:
        if x>z:
            print(f"{y}<{z}<{x}")
        elif x<z:
            print(f"{y}<{x}<{z}")
        else:
            print(f"{z}={x}<{y}")
