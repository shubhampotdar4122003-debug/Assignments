import os
def directory(filename):
    
    ret = os.path.exists(filename)
    if ret == False:
        print("there is no such Directory")
    else:
        print("there is such Directory")
        
        file = open(filename,'r')
        line = (file.read())
        words = line.split()

        print("Total number of words in Demo.txt are :",len(words))
        
        file.close()
    
def main():
    filename = input("Enter the filename :")
    
    directory(filename)
if __name__ == "__main__":
    main()