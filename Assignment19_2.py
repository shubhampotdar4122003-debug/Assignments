def main():
    no1 = int(input("Enter the First  number :"))
    no2 = int(input("Enter the Second number :"))
    
     
    Mult = lambda a,b : a * b
    
    print("The Answer is :",Mult(no1,no2))


if __name__ =="__main__":
    main()