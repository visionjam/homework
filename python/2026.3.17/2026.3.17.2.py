def jitu():
    a=int(input("请输入总数M:"))
    b=int(input("请输入总脚数N:"))

    if b %2!=0:
        print("数据错:脚数N必须是偶数")
        return
    else:
        tu=b/2-a
        ji=a-tu

        if ji<=0 or tu<=0:
            print("数据错：求出的头数不能为负数")
            return
        else:
            print(f"鸡有{ji:.0f}只")
            print(f"兔有{tu:.0f}只")

jitu()