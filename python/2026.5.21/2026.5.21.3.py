class Rect:
    """设计一个矩形类"""
    def __init__(self,a,b):
        self.lenth=a
        self.width=b

    def perimeter(self):
        perimeter=2*(self.lenth+self.width)
        return(perimeter)
    
    def square(self):
        square=self.lenth*self.width
        return(square)
    
    def output(self):
        print(f"长：{self.lenth}, 宽：{self.width}")
        print(f"周长：{self.perimeter()}, 面积：{self.square()}")

        return
    
    def Sum(self,other):
        add=self.square()+other.square()
        return add
    
if __name__ == "__main__":
    r1=Rect(4,5)
    r2=Rect(3,6)

    print(f"矩形1：")
    r1.output()
    print(f"矩形2：")
    r2.output()

    totalsquare=r1.Sum(r2)
    print(f"矩形1和矩形2的面积和：{totalsquare}")