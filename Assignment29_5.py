
import os

def filename(file,word):
    
    ret = os.path.exists(file)
    if ret == False:    
        print("there is no such Directory")
    else:
        print("there is such Directory")
        
    file= open(file,'r')
    
    contents = file.read()
    count = contents.count(word)
    print(count)
    file.close()
        
def main():
    file = input("enter the filename :")
    word = input("Enter the word :")
    
    filename(file,word)

if __name__ == "__main__":
    main()