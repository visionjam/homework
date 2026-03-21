import random
random.seed(100)
a=random.randint(1,100)
attempt=0
while True:
    guess=int(input("请输入您的猜测数："))
    attempt+=1

    if guess<a:
        print("小了！")
    elif guess>a:
        print("大了！")
    else:
        print(f"恭喜您！您猜中了！共猜测{attempt}次。")
        break