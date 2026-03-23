class BankAccount:
    ROI = 10.5
    
    def __init__(self):
        self.Name = "Shubham potdar"
        self.Amount = 1000
        
    def display(self):
        print("The Bank holder name is :",self.Name,"and the Balance is :",self.Amount)
        
        
        
    def Deposit(self):
        self.num = int(input("Enter the diposite Ammount :"))
        self.Balance = self.num +self.Amount
        print("After  Deposited the total  Ammount is : ",self.Balance)
        
      
    def withdraw(self):
        self.withdrw = int(input("Enter the withdraw amount:"))
        remained_Balance =self.Balance - self.withdrw
        print("The Ammount after Withdrawal :",remained_Balance)
        
    def calculateInterest(self):
        self.Interest = (self.Balance * BankAccount.ROI )/100
        print("The total interest after calculating :",self.Interest)   
        
obj = BankAccount()
obj.display() 
obj.Deposit()  
obj.withdraw()  
obj.calculateInterest()  

print()

obj1 = BankAccount()
obj1.display() 
obj1.Deposit()  
obj1.withdraw()  
obj1.calculateInterest() 
             
        
        
        
                
    
    