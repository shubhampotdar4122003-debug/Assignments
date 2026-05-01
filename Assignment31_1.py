

import os
import sys


def search_files(directory_name, extension):
    try:
        files = os.listdir(directory_name)

        found = False

        for file in files:
            full_path = os.path.join(directory_name, file)

            if os.path.isfile(full_path):
                if file.endswith(extension):
                    print(file)
                    found = True

        if not found:
            print("No files found with extension", extension)

    except Exception as e:
        print("Error :", e)


def main():
    if len(sys.argv) != 3:
        print("Usage : python DirectoryFileSearch.py <DirectoryName> <Extension>")
        return

    directory_name = sys.argv[1]
    extension = sys.argv[2]

    if not os.path.isdir(directory_name):
        print("Directory does not exist")
        return

    search_files(directory_name, extension)


if __name__ == "__main__":
    main()