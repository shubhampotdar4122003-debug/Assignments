class Arithmatic :
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        
    def Accept(self):
        self.value1 = int(input("Enter the first value :"))
        self.value2 = int(input("Enter the second value :"))
        
    def Addition(self):
        self.addition = self.value1 + self.value2
        return self.addition        
    
    def Substraction(self):
        self.sub = self.value1 - self.value2
        return self.sub  
    
    def Multiplication(self):
        self.mult = self.value1 * self.value2
        return self.mult
    
    def Division(self):
        try : 
            self.div = self.value1 / self.value2
            return self.div
        except ZeroDivisionError as zobj:
            print("The number is ",zobj)
            
        finally :
             print(" is not defined")   
    
    def ans(self):
        print("The Addition of both values :",self.addition) 
        print("The substraction of both values :",self.sub)
        print("The Multiplicationtion of both values :",self.mult)
     
obj = Arithmatic()
obj.Accept()        
obj.Addition()
obj.Substraction()
obj.Multiplication()
obj.Division()
obj.ans()

print()

obj1 = Arithmatic()
obj1.Accept()        
obj1.Addition()
obj1.Substraction()
obj1.Multiplication()
obj1.Division()
obj1.ans()