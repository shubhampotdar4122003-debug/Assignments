
    
from functools import reduce

def prime(num):
    
    if num <= 1 :
        return False
    
    for i in range(2,num):
        if(num % i == 0):
            return False
    return True   
                

def main():
    
     number = int(input("Enter the elements :"))
     Data = []
    
     for i in range(number):
         num = int(input(f"enter the element{i + 1} :"))
         Data.append(num)
        
     fdata = list(filter(prime,Data))
     print("The data after filter :",fdata)
        
     mdata = list(map(lambda a : a*2,fdata))
     print("the data after map :",mdata)
        
     rdata = (reduce(lambda a,b :a if a > b else b,mdata))
     print("the data after reduce :",rdata)
    
if __name__ =="__main__":
    main()   

    
        
                
    
    
    
    
  

