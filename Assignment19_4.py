
    
from functools import reduce
def main():
    number = int(input("Enter the elements :"))
    Data = []
    
    for i in range(number):
        num = int(input(f"enter the element{i + 1} :"))
        Data.append(num)
        
    fdata = list(filter(lambda a : a % 2 == 0,Data))
    print("The data after filter :",fdata)
        
    mdata = list(map(lambda a : a*a,fdata))
    print("the data after map :",mdata)
        
    rdata = (reduce(lambda a,b : a + b,mdata))
    print("the data after reduce :",rdata)
    
if __name__ =="__main__":
    main()   

    
        
                
    
    
    
    
  

