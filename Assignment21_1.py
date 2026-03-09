import threading

def prime(numbers):
    print("the all value are prime number : ")
    for num in numbers:
        if num > 1 :  
           
            for i in range(2,num):
                if(num % i == 0):
                    break
            else :
                print(num)
                        
def Non_prime(numbers):
    print("the all value are non prime number : ")
    for num in numbers :
        if num > 1 :
    
            for i in range(2,num):
                if(num % i == 0):       
                    print(num)
                    break
                      
def main():
    numbers = list(map(int,input("Enter the numbers :").split()))
    
    t1 = threading.Thread(target=prime,args = (numbers,))
    t2 = threading.Thread(target=Non_prime,args = (numbers,))
     
    t1.start()
    t1.join()
      
    t2.start()
    t2.join()
      
if __name__ =="__main__":
    main()   

    
        
                
    
    
    
    
  

