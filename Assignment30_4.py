import os
def directory(filename,sec_filename):
    
    ret = os.path.exists(filename) or os.path.exists(sec_filename)
    if ret == False:
        print("there is no such Directory")
    else:
        print("there is such Directory")
        
        file = open(filename,'r')
        contents = file.read()
        
        sec_filename = open(sec_filename,'w')
        print(contents,file=sec_filename)
        
        print("contents of ABC.txt file are copied to Demo.txt file")
        file.close()
    
def main():
    filename = input("Enter the filename :")
    sec_filename = input("Enter the second filename :")
    
    
    directory(filename,sec_filename)
if __name__ == "__main__":
    main()