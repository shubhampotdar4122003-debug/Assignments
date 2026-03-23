class Numbers :
    
    def __init__(self):
        self.value = int(input("Enter the value :"))
        
    def chkprime(self):
        
        prime = 0
        for i in range(1,self.value+ 1):
            if(self.value % i == 0):
                prime += 1
        if(prime == 2):
            
            print(True)
            
        else :
            print(False)            
            
    def chkperfect(self):
        sum = 0
        for i in range(1,self.value):
            if(self.value % i == 0):
                sum  += i
                
        if sum == self.value:        
            print("it is an perfect",self.value)
        else:
            print("its not perfect number:",self.value)  
            
    def factors(self):
        
        for i in range(1,self.value):
            if(self.value % i == 0):    
                print("the factors is :",i)
    def sumfactor(self):
        sum = 0
        for i in range(1,self.value):
            if(self.value % i == 0):
                sum += i 
        print("the sum factors is:",sum)               
  
obj = Numbers()

obj.chkprime()
obj.chkperfect()
obj.factors()
obj.sumfactor()

print()
obj1 = Numbers()
obj1.chkprime()
obj1.chkperfect()
obj1.factors()
obj1.sumfactor()


         