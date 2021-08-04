class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectangle():
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def get_area(self):
        return (self.p2.x-self.p1.x)*(self.p1.y-self.p2.y)
    def get_perimeter(self):
        return 2*((self.p2.x-self.p1.x)+(self.p1.y-self.p2.y))
    def is_square(self):
        return (self.p2.x-self.p1.x) == (self.p1.y-self.p2.y)

p3 = Point(1,3)
p4 = Point(3,1)
r1 = Rectangle(p3,p4)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p5 = Point(3,7)
p6 = Point(6,4)
r2 = Rectangle(p5,p6)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())