phone_book = {}
while True:
    print("请输入姓名和手机号（格式：张斌 13401279012），输入-1结束：", end="")
    user_input = input()
    print()
    parts = user_input.split()
    if user_input == "-1":
        break
    if len(parts) == 2:
        name = parts[0]
        phone = parts[1]
        phone_book[name] = phone

while True:
    print("请输入要查找的姓名，输入“xxx”结束：", end="")
    search_name = input()
    if search_name == "xxx":
        print()
        break
    if search_name in phone_book:
        print(f"{search_name}的手机号码是{phone_book[search_name]}")
        print()
    elif search_name not in phone_book:
        print(f"没有找到{search_name}的手机号码")
        print()