

import os
import sys


def rename_files(directory_name, old_extension, new_extension):
    try:
        files = os.listdir(directory_name)

        found = False

        for file in files:
            old_path = os.path.join(directory_name, file)

        
            if os.path.isfile(old_path):

                
                if file.endswith(old_extension):

                    
                    new_name = file[:-len(old_extension)] + new_extension
                    new_path = os.path.join(directory_name, new_name)

                    os.rename(old_path, new_path)

                    print(file, "renamed to", new_name)
                    found = True

        if not found:
            print("No files found with extension", old_extension)

    except Exception as e:
        print("Error :", e)


def main():
    if len(sys.argv) != 4:
        print("Usage : python DirectoryRename.py <DirectoryName> <OldExt> <NewExt>")
        print("Example : python DirectoryRename.py Demo .txt .doc")
        sys.exit()

    directory_name = sys.argv[1]
    old_extension = sys.argv[2]
    new_extension = sys.argv[3]

    if not os.path.isdir(directory_name):
        print("Directory does not exist")
        sys.exit()

    rename_files(directory_name, old_extension, new_extension)


if __name__ == "__main__":
    main()