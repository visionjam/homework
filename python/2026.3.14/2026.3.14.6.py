name="张三"
age=19
height=1.85

print("我的名字是",name,",","我",age,"岁了",",","身高",height,"米。",sep="")
print("我的名字是%s,我%d岁了,身高%.2f米。"%(name,age,height))
print("我的名字是{},我{}岁了,身高{}米。".format(name,age,height))