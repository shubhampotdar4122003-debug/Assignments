import threading



def Thread1():
    print("The Number from 1 to 50 are :")
    for i in range(1,51):
        print(i)
        
                
                    
def Thread2():
    print("The Reverse Numbers from 50 to 1 are :")
    for i in range(50,0,-1):
        print(i)
    
           
            

            
            
def main():
    
    
    t1 = threading.Thread(target=Thread1)
    t2 = threading.Thread(target=Thread2)
    
    
    t1.start()
    t1.join()
    
    
    t2.start()
    t2.join()
    
    
    
    
if __name__ =="__main__":
    main()   

    
        
                
    
    
    
    
  

