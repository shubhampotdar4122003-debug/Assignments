def chknum(num):
    
    if(num % 2 == 0):
        print("Even NUmber")
    else :
        print("Odd Number")    
    
    
def main():
    num = int(input("Enter the number :"))
    chknum(num)

if __name__ == "__main__":
    main()  