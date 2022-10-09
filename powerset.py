class PowerSet():
    def _init_(self,x):
        if type(x)==set:
            self.x=x
        else:
            print("not a set")
    def _add_(self,other):
        print('1st set : ',self.x)
        print("2nd set: ",other.x)
        print("Union result: ",self.x.union(other.x))
    def _mul_(self,other):
        print('1st set : ',self.x)
        print("2nd set: ",other.x)
        print("Intersection result: ",self.x.intersection(other.x))
    def _sub_(self,other):
        print('1st set : ',self.x)
        print("2nd set: ",other.x)
        print("difference result: ",self.x.difference(other.x))