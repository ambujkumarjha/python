class StLine:
    def __init__(self,l=None):
        if l is None:
            self.length=eval(input("Enter the length:"))
        else:
            self.length=l
        print("Object of StLine has created")
    def display(self):
        return self.length
class Square(StLine):
    def __init__(self,l=None):
        if l is None:
            super().__init__()
        else:
            super().__init__(l)
        print("Object of Square has created")
    def calc_area(self):
        return self.length*self.length
    def display(self):
        return self.length
class Cube(StLine):
    def __init__(self,l=None):
        if l is None:
            super().__init__()
        else:
            super().__init__(l)
        print("Object of Cube has created")
    def calc_area(self):
        return self.length*self.length*6
    def display(self):
        return self.length
r=eval(input("Enter the radius "))
h1=Cube(r)
h2=StLine(r)
h3=Square(r)
print(h1.display())
print(h3.calc_area())
print(h1.display())
print(h1.calc_area())
