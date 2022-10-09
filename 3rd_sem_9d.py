class SqrArea:
    def __init__(self,l=None):
        if l is None:
            self.length=eval(input("Enter the length:"))
        else:
            self.length=l
        print("Object SqrArea has created....")
    def calc_Area(self):
        return self.length*self.length
    def _del_(self):
        print("Object has been destructed 123")
class SqrPeri:
    def __init__(self,l=None):
        if l is None:
            self.length=eval(input("Enter the length:"))
        else:
            self.length=l
        print("Object SqrPeri has created....")
    def cal_Area(self):
        return 4*self.length
    def _del_(self):
        print("Object has been destructed 123")
class Square(SqrArea,SqrPeri):
    def __init__(self,l=None):
        if l is None:
            super().__init__()
        else:
            super().__init__(l)
        print("Object Square has created")
    def Show(self):
        return super().cal_Area(),super().calc_Area()
    def _del_(self):
        print("Object has been destructed 123")
r=eval(input("Enter the length:"))
p=SqrArea(r)
print("Area of a square:")
print(p.calc_Area())
m=SqrPeri(r)
print(m.cal_Area())
y=Square(r)
print(y.Show())
