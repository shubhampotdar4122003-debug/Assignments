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

        
def DeleteDuplicateFiles(duplicates):

    file = open("Log.txt", "w")

    count = 0

    for key in duplicates:

        if len(duplicates[key]) > 1:

            # Keep first file
            original = duplicates[key][0]

            file.write("Original File Kept : " + original + "\n")

            # Delete remaining duplicate files
            for duplicate in duplicates[key][1:]:

                os.remove(duplicate)

                file.write("Deleted File : " + duplicate + "\n")

                count += 1

            file.write("\n")

    
            
                
            
            
    file.close()
    
    return count
        

def main():
    
    duplicate = findduplicate()
    
    DeleteDuplicateFiles(duplicate)
 
    
    
    

if __name__ == "__main__":
    main()