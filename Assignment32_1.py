import hashlib
import os

def checksum(fname):
    
    file = open(fname,'rb')
    
    hash = hashlib.md5()
    
    read = file.read(1000)
    
    while(len(read)>0):
        hash.update(read)
        read = file.read(1000)
        
    file.close()
    
    return hash.hexdigest()    

def Directory(filename):
    
    ret = False
    
    ret = os.path.exists(filename)
    if ret == False:
        print("There is no such file exists")
        return

    
    ret = os.path.isdir(filename)
    
    if ret == False:
        print("There is no such Directory")
        return
    
    for FolderName,SubFolderName,FileName, in os.walk(filename):
        
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            check = checksum(fname)
            
            print("files:",fname or "checksum value :",check)
            
                

def main():
    
    Directory("Demo")

if __name__ =="__main__":
    main()