s=input("请输入一个字符句子：")
for i in s.split(" "):
    len(i)
print(f"最长的单词是:{max(s.split(" "))},长度是:{len(max(s.split(" ")))}")