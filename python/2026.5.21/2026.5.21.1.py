import math
class Building:
    """设计一个楼房类"""
    def setvalue(self,a,b,c,d):
        self.lenth=a
        self.width=b
        self.floor=c
        self.price=d
    def square(self):
        sq=self.lenth*self.width*self.floor
        return(sq)
    
    def totalprice(self):
        tp=self.lenth*self.width*self.floor*self.price
        return(tp)
    
result=Building()
result.setvalue(10,20,5,5000)
resultsquare=result.square()
resultprice=result.totalprice()
print(f"楼房的面积：{resultsquare}平方米")
print(f"楼房的总价：{resultprice}元")