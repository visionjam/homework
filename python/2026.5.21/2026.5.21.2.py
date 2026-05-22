class identifier:
    """定义一个identifier类"""
    def __init__(self,a):
        self.id=a

    def getyear(self):
        a1=str(self.id) 
        year=a1[6:10]
        return(year)
    def Disp(self):
        return(self.id)
    
idinput=input("请输入一个身份证号：")
result=identifier(idinput)
resultyear=result.getyear()
resultid=result.Disp()

print(f"出生年份：{resultyear}")
print(f"身份证号码：{resultid}")