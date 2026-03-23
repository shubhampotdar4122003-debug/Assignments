class circle :
    PI = 3.14
    

    def __init__(self):
        self.radius = 0.0
        self.Area = 0.0
        self.Circumference= 0.0
        
        
    def Accept(self):
        self.radius = float(input("Enter the value of radius :"))
        
    def calculateArea(self):
        self.Area = circle.PI * self.radius * self.radius
        
    def calculatecircumference(self):
        self.circumference = 2 * circle.PI * self.radius
        
    def display(self):
        print("The value of Radius :",self.radius) 
        print("The Area of circle :",self.Area)
        print("The circumference of circle :",self.circumference)
        

obj=circle()
obj.Accept()
obj.calculateArea()
obj.calculatecircumference()
obj.display() 

print()

obj1=circle()
obj1.Accept()
obj1.calculateArea()
obj1.calculatecircumference()
obj1.display()

                  
        
          