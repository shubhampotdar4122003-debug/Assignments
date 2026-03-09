import threading



def Evenlist(num):
    
    
    sumeven = 0
    for i in num :
        if (i % 2 == 0):
            print(i)
            sumeven += i
    print("The sum of evenlist :",sumeven)
            
            
                    
def Oddlist(num):
    
    
    
        
    sumodd = 0
    for i in num :
        if(i % 2 != 0):
            print(i)
            sumodd += i
    print("The sum of oddlist :",sumodd)
            
            
def main():
    Data =[10,11,12,13,14,15,16]
    
    t1 = threading.Thread(target=Evenlist,args =(Data,))
    t2 = threading.Thread(target=Oddlist,args = (Data,))
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()
    
if __name__ =="__main__":
    main()   

    
        
                
    
    
    
    
  

