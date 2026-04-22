import os
import sys
def Filename(dirname = "Abc.txt"):
    
    ret =os.path.exists(dirname)
    
    if ret == False :
        print("there is no exists such Directory")
    else :
        print("there is such Directory")
       
        fobj =open('Abc.txt','r')
        f =fobj.read()
        
        
        file = open('Demo.txt','w')
        file.write(f)
        print("the contents from previous file is copied successfully")
        
        file.close()
        
    
def main():
    
    
    if(len(sys.argv) != 2):
        print("the Arguments are invalid")
        print("enter the valid number of Arguments")
        return
    
    Filename(sys.argv[1])
if __name__ == "__main__":
    main()