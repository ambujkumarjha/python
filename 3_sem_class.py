class Circle():
    def init(self,r=None):
        if r is None:
            self.radious = eval(input('enter the radius: '))
        else:
            self.radius = r
            print("a circle has been created")
        
    def get_radius(self):
        return self.radius
    
    def calc_area(self):
        return 3.14*self.radius**2
    
    def del(self):
    print("object destroyed")