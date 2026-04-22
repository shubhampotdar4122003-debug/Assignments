import os
import sys

def Filename(value1, value2 ):

    ret = os.path.exists(value1) or os.path.exists(value2)
    if ret == False :
        print("There is no such Directory")
        
    else :
        print("Theere is Directory")
        
        file1 = open(value1,'r')
        file2 = open(value2,'r')
        
        if file1.read() == file2.read() :
            print("Success")
        else:
            print("Failure")                         
          
def main():
    if(len(sys.argv) != 3):
        print("the Arguments are invalid")
        print("enter the valid number of Arguments")
    else :    
    
        Filename(sys.argv[1], sys.argv[2])
    
if __name__ == "__main__":
    main()
    

       