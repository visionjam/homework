file_path = r"C:\Users\29576\Downloads\学生成绩文件.txt"
scores = []
with open(file_path, "r", encoding="gbk") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 3:
            try:
                score = float(parts[-1]) 
                scores.append(score)
            except ValueError:
                continue

if scores:
    average = sum(scores) / len(scores)
    minimum = min(scores)
    maximum = max(scores)
    print(f"平均分：{average:.1f}")
    print(f"最低分：{minimum:.1f}")
    print(f"最高分：{maximum:.1f}")