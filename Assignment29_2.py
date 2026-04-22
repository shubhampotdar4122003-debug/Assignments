import os
def Filename(dirname = "Demo.txt"):
    

    
    
    ret =os.path.exists(dirname)
    
    if ret == False :
        print("there is no exists such Directory")
    else :
        print("there is such Directory")
        
        file = open('Demo.txt','r')
        print("The contents from directory are :")
        contents = file.read()
        print(contents)
        file.close()
        
    
def main():
    directoryname = input("Enter the Directory Name :")
    
    Filename(directoryname)
if __name__ == "__main__":
    main()