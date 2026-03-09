
    
from functools import reduce

greater = lambda a :90 >= a >=70
increment = lambda a : a + 10 
product = lambda a,b : a * b

def main():
    num = int(input("enter the number of elements :"))
    Data =[]
    for i in range(num):
        number = int(input(f"Enter the elements {i + 1} :"))
        Data.append(number)
    
    fdata = list(filter(greater,Data))
    print("The Data after the filter :",fdata)
    
    mdata = list(map(increment,fdata))
    print("the data after map :",mdata)
    
    rdata = (reduce(product,mdata))
    print("the data after reduce :",rdata)
    
if __name__ =="__main__":
    main()   

    
        
                
    
    
    
    
  

