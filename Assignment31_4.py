
import os
import sys
import shutil

def copy_with_extension(src, dest, ext):
    if not os.path.exists(src):
        print("Source directory does not exist")
        return

    os.makedirs(dest, exist_ok=True)

    for file in os.listdir(src):
        src_path = os.path.join(src, file)
        dest_path = os.path.join(dest, file)

        if os.path.isfile(src_path) and file.endswith(ext):
            shutil.copy(src_path, dest_path)

    print(f"All {ext} files copied successfully")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('Usage: python DirectoryCopyExt.py "Demo" "Temp" ".exe"')
    else:
        copy_with_extension(sys.argv[1], sys.argv[2], sys.argv[3])