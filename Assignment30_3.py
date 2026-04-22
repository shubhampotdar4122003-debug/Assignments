import os
def directory(filename):
    
    ret = os.path.exists(filename)
    if ret == False:
        print("there is no such Directory")
    else:
        print("there is such Directory")
        print("displayed each line by line from Demo.txt file :")
        
        file = open(filename,'r')
    
        for line in file:
            print(line,end="")
        file.close()
    
def main():
    filename = input("Enter the filename :")
    
    directory(filename)
if __name__ == "__main__":
    main()