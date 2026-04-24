d={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
number=input("请输入电话号码：")
a=[]
for char in number:
    a+=char
phone=list(map(d.get,a))
for char in phone:
    print(char,end=" ")