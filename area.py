import sys
class Shape:
    def __init__(self):
        pass
class Hexagon(Shape):
    def __init__(self,s):
        self.s=s
    def calcArea(self):
        AreaOfHexagon=1.5*1.732*self.s
        return AreaOfHexagon
    def calcPeri(self):
        PerimeterOfHexagon=6*self.s
        return PerimeterOfHexagon
    def calcAngleSum(self):
        Sumofangles=6*120
        return Sumofangles
    def display(self):
        area=self.calcArea()
        peri=self.calcPeri()
        add=self.calcAngleSum()
        print(" The area of hexagon is : ",area)
        print(" The perimeter of hexagon is : ",peri)
        print(" The sum of all angles of hexagon is : ",add)

class Square(Shape):
    def __init__(self,length):
        self.length=length
    def calcAreaSquare(self):
        AreaOfSquare=self.length*self.length
        return AreaOfSquare
    def calcPeriSquare(self):
        PerimeterOfSquare=4*self.length
        return PerimeterOfSquare
    def display(self):
        area=self.calcAreaSquare()
        perimeter=self.calcAreaSquare()
        print("Area of Square is :",area)
        print(" The Perimeter of square is : ",perimeter)
        
        
def main():
    hexagon=Hexagon(8)
    square=Square(9)
    while True:
        print("\n \tEnter 1 to calculate area, perimeter and sum of all angles of hexagon :")
        print("\n \tEnter 2 to calculate area and perimeter of square :")
        user=input()
        if user== '1':
            hexagon.display()
        elif user== '2':
            square.display()
        else:
            sys.exit("Exiting the program ")
if __name__ == "__main__":
    main()

