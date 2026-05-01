import os
import hashlib

def calculatechecksum(filename):
    
    file = open(filename,'rb')
    
    hash = hashlib.md5()
    
    read = file.read(1000)
    
    while(len(read)>0):
        hash.update(read)
        read = file.read(1000)
        
    file.close()
    
    return hash.hexdigest()    

def findduplicate(Directoryname = "demo"):
    
    ret = False
    ret = os.path.exists(Directoryname)
    if ret == False:
        print("There is no such Directory")
        return
    
    ret = os.path.isdir(Directoryname)
    if ret == False:
        print("There is no such directory exists")
        return
    
    Duplicate ={}
    for FolderName,SubFolderName,FileName in os.walk(Directoryname):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            checksum = calculatechecksum(fname)
            
            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
                
            else:
                Duplicate[checksum] = [fname]    
                
    return Duplicate

        
def create_log(duplicate):
    
    new_file = open("log.txt",'w')
    
    for key in duplicate:
        
        if len(duplicate[key])>1:
            new_file.write("duplicate files\n")
            
            for fname in duplicate[key]:
                new_file.write(fname + "\n")
            new_file.write("\n")
            
    new_file.close()
 

    
    
           

def main():
    
    duplicate = findduplicate()
    
    create_log(duplicate)
    
    
    

if __name__ == "__main__":
    main()