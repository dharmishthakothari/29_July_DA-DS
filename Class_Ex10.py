class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"{self.x} : {self.y}"
    def __add__(self,other):
        #p3=Point(self.x+other.x,self.y+other.y)
        p3=Point(self.x+self.y,other.x+other.y)
        return p3
    def __ge__(self,other):
        if self.x>other.x:
            return True
        

p1 = Point(23,12)
p2 = Point(28,5)
print(p1)
print(p2)
print(p1+p2)
print(p1>=p2)