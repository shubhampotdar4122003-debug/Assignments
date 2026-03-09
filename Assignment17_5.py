
def main():
    
    prime = 0
    no = int(input("enter the number :"))
    for i in range(1,no + 1):
        if (no % i == 0) :
            prime += 1
    if prime == 2:        
        print("it is an prime number")
    else :
        print("it is not an prime number")        
        


if __name__ =="__main__":
    main()
    
    
    
  
                



    


