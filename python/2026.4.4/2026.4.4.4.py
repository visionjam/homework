import random
random.seed(400)
a = []
for i in range(0, 30):
    b = random.randint(0, 100)
    a += [b]

def MyFun(scores, grade=5):
    excellent = 0
    good = 0
    medium = 0
    pass_grade =0
    fail = 0

    for score in scores:
        if score >= 90:
            excellent += 1
        elif score >= 80:
            good += 1
        elif score >= 70:
            medium += 1
        elif score >= 60:
            pass_grade += 1
        else:
            fail += 1

    if grade == 5:
        print(f"优秀人数： {excellent}")
    elif grade == 4:
        print(f"良好人数： {good}")
    elif grade == 3:
        print(f"中等人数： {medium}")
    elif grade == 2:
        print(f"及格人数： {pass_grade}")
    elif grade == 1:
        print(f"不及格人数： {fail}")

MyFun(a, 3)
MyFun(a, grade=4)
MyFun(a)