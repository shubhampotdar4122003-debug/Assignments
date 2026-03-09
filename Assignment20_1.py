import threading

  
def Even():
    
    for i in range(2,11):
        if (i % 2 == 0):
            print("First Even numbers are :",i)
                    
def Odd():
    
    for i in range(1,10):
        if(i % 2 != 0):
            print("First odd numbers are :", i)
def main():
    
    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
    
    
if __name__ =="__main__":
    main()   

    
        
                
    
    
    
    
  

