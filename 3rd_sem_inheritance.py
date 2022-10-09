class StLine():
    def __init__(self,l=None):
        if l is None :
            self.length=eval(input("Enter the hight ;"))
        else:
            self.length=1
    print('A stright line has been created')
    def get_length(self):
        return self.length
    def __del__(self):
        print("object destructed")
class square(StLine):
    def __init__(self,l=None):
        if l is None:
         super().__init__()
        else:
            super().__init__(l)
        print("A square has been created")
    def clac_area(self):
        return self.length**2
class cube(square):
    def __init__(self,h=None):
        if h is None:
         super().__init__()
        else:
            super().__init__(l)
        print("A cube has been created")
        if h is None:
            self.height=eval(input("enter the value of height:"))
        else:
            self.height=h
    def clac_area(self):
        return self.height*self.height*6
h=eval(input())
l=eval(input())
h1=cube(h)
h2=StLine
print(h1.clac_area())
        
    