n = int(input("请输入员工人数(<10)："))
employees = []

for i in range(n):
    line = input("请输入工号、姓名、奖金，空格分隔：")
    id, name, bonus = line.split()
    employees.append([id, name, bonus])

with open("JJ.txt", "w", encoding="utf-8") as f:
    for emp in employees:
        f.write(f"{emp[0]},{emp[1]},{emp[2]}元\n")

with open("JJ.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

parsed = []
for line in lines:
    line = line.strip()
    if not line:
        continue
    id, name, bonus_str = line.split(",")
    bonus = float(bonus_str.rstrip("元"))
    parsed.append([id, name, bonus])

parsed.sort(key=lambda x: x[2])
with open("NewJJ.txt", "w", encoding="utf-8") as f:
    for emp in parsed:
        f.write(f"{emp[0]},{emp[1]},{emp[2]:.1f}元\n")