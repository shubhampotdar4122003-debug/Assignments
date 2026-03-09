import threading

num = int(input("Enter the number :"))  
def EvenFactor(num):
    sumevenfactor = 0
    print("The evenfactors are :")
    for i in range(1,num+1):
        if (i % 2 == 0 and num % i == 0):
            print(i)
            sumevenfactor += i
            print("The sum of EvenFactors numbers are :",sumevenfactor)
                    
def OddFactor(num):
    sumoddfactor = 0
    print("The oddfactors are :")
    for i in range(1,num +1):
        if(i % 2 != 0 and num % i == 0):
            print(i)
            sumoddfactor += i
            print("The sum of oddFactors numbers are :", sumoddfactor)
            
            
def main():
    
    t1 = threading.Thread(target=EvenFactor,args =(num,))
    t2 = threading.Thread(target=OddFactor,args = (num,))
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
    
print("Exit from main")  

    
if __name__ =="__main__":
    main()   

    
        
                
    
    
    
    
  

