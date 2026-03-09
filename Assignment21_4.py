import threading



number =[1,2,3,4,5,6]

def sum_elements():
    
    total = sum(number)
    print("The sum of element from list are",total)
    
    
def product_elements():
    
    product = 1
    for num in number:
        product *= num
    print("the product of elements are :",product)    
        
def main():
    
    
    
    t1 = threading.Thread(target=sum_elements)
    t2 = threading.Thread(target=product_elements)
    
    t1.start()
    t1.join()
    
    
    t2.start()
    t2.join()
     
    print("Both threads completed")
if __name__ =="__main__" :
    main()