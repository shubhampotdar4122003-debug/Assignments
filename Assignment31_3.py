
import os
import sys
import shutil

def copy_directory(src, dest):
    if not os.path.exists(src):
        print("Source directory does not exist")
        return
    os.makedirs(dest, exist_ok=True)

    for file in os.listdir(src):
        src_path = os.path.join(src, file)
        dest_path = os.path.join(dest, file)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)

    print("All files copied successfully")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python DirectoryCopy.py "Demo" "Temp"')
    else:
        copy_directory(sys.argv[1], sys.argv[2])