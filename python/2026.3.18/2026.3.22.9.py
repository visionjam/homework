days = {1: "周一",2: "周二", 3: "周三",4: "周四",5: "周五",6: "周六"}
for x in range(1, 5):
    for y in range(x + 1, 6):
        for z in range(max(5, y + 1), 7):
            print(f"x - {days[x]},y - {days[y]},z - {days[z]}")