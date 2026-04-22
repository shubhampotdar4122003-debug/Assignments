import os
def directory(filename):
    
    ret = os.path.exists(filename) 
    if ret == False:
        print("there is no such Directory")
    else:
        print("there is such Directory")
        
        word = input("Enter the word :")
        
        file = open(filename,'r')
    
        contents = file.read()
        if word in contents:
            print("The word is found in Demo.txt file")
            
        else:
            print("The word is not found in Demo.txtfile")
            
        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        file.close()
    
def main():
    filename = input("Enter the filename :")
    
    
    
    
    directory(filename)
if __name__ == "__main__":
    main()