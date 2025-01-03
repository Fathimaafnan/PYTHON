class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    def area(self):
        return self.__length*self.__breadth
    def __lt__(self,other):
        if self.area()<other.area():
            return True
        else:
            return False
r1=Rectangle(5,6)
r2=Rectangle(7,8)
if r1<r2:
    print("r1 is less")
else:
    print("r2 is less")