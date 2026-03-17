s=float(input("请输入成绩："))

if s<60:
    print(f"成绩:{s:.2f}, 绩点:0")
elif 60<=s<=69:
    print(f"成绩:{s:.2f}, 绩点:1")
elif 70<=s<=79:
    print(f"成绩:{s:.2f}, 绩点:2")
elif 80<=s<=89:
    print(f"成绩:{s:.2f}, 绩点:3")
elif 90<=s<=100:
    print(f"成绩:{s:.2f}, 绩点:5")
else:
    print("输入成绩的格式不对")