class Square:
    def __init__(self, long):
        self.long = long


class Shape(Square):
    def __init__(self, long):
        super().__init__(long)

    def area(self, long):
        print(self.long * 0)
class Rectangle(Shape):
    def __init__(self, long, weit):
        super().__init__(long)
        self.weit = weit
    def area2(self, init, *weit):
        print("The are is:", self.long * self.weit)


long = Rectangle(int(input("Enter the long: ")), int(input("Enter the weit: ")))
long.area2(long)