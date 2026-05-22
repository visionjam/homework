class Person:
    """设计一个Person类"""
    def __init__(self,a,b):
        self.Name=a
        self.Age=b

    def Disp(self):
        print(f"姓名：{self.Name}, 年龄：{self.Age}")
        return

    
class Teacher(Person):
    def __init__(self,a,b,c,d):
        Person.__init__(self,a,b)
        self.No=c
        self.Ta=d

    def NewDisp(self):
        self.Disp()
        print(f"工号：{self.No}, 教龄：{self.Ta}")
        return
    
Teacher=Teacher("张老师",45,"2006010",14)
Teacher.NewDisp()