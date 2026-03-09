import threading



def Uppercase(str):
    print("Thread ID :",threading.get_ident())
    print("Thread Name :",threading.current_thread().name)
    
    upper = 0
    for ch in str:
        if ch.isupper():
            print(ch)
            upper += 1
    print("the total uppercase is :",upper)            
                    
def Lowercase(str):
    print("Thread ID :",threading.get_ident())
    print("Thread Name :",threading.current_thread().name)
    lower = 0
    for ch in str:
        if ch.islower():
            print(ch)
            lower += 1
    print("the total lower is :",lower) 
           
    
def numeric(str):
    print("Thread ID :",threading.get_ident())
    print("Thread Name :",threading.current_thread().name)
    numeric = 0
    for ch in str:
        if ch.isdigit():
            print(ch)
            numeric += 1
    print("The total digit are :",numeric)            

            
            
def main():
    case = ("MARVELLOUSinfosystem123")
    
    t1 = threading.Thread(target=Uppercase,args =(case,))
    t2 = threading.Thread(target=Lowercase,args = (case,))
    t3 = threading.Thread(target = numeric,args = (case,))
    
    t1.start()
    t1.join()
    
    t2.start()   
    t2.join()
    
    t3.start()
    t3.join()
    
    
if __name__ =="__main__":
    main()   

    
        
                
    
    
    
    
  

