import threading

def Maximum(numbers):
    print("the  numbers : ")
    max_num = numbers[0]
    
    for num in numbers:
        if num > max_num:
            max_num = num
        
    print("the maximum elements in list : ",max_num)
    
    
                        
def Minimum(numbers):
    print("The numbers")
    min_num = numbers[0]
    
    for num in numbers:
        if num < min_num:
            min_num = num
            
    print("The minimum elements from list :",min_num)        
    
                      
def main():
    numbers = list(map(int,input("Enter the numbers :").split()))
    
    t1 = threading.Thread(target=Maximum,args = (numbers,))
    t2 = threading.Thread(target=Minimum,args = (numbers,))
     
    t1.start()
    t1.join()
      
    t2.start()
    t2.join()
      
if __name__ =="__main__":
    main()   

    
        
                
    
    
    
    
  

