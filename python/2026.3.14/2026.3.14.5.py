id=input("请输入18位身份证号码：")
s1=id[6:10]
s2=id[10:12]
s3=id[12:14]
print(f"身份证号码是:{id}")
print(f"{s1}年{s2}月{s3}日")