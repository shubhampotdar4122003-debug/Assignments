
def main():
    num = int(input("Enter the number:"))
    sum= 0

    while num > 0:
        digit = num % 10
        sum += digit
        num = num // 10
    
    print("sum of digits",sum)
if __name__ =="__main__":
    main()
    
    
    
  
                



    


