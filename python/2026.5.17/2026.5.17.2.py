file_path = r"C:\Users\29576\Downloads\T1.txt"
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

line_count = len(lines)
print(f"文件的行数：{line_count}")

converted_lines = []
for line in lines:
    new_line = ''
    for ch in line:
        if 'a' <= ch <= 'z':
            new_line += ch.upper()
        elif 'A' <= ch <= 'Z': 
            new_line += ch.lower()
        else:
            new_line += ch
    converted_lines.append(new_line)
    print(new_line, end="")

with open('T2.txt', 'w', encoding='utf-8') as f:
    f.writelines(converted_lines)