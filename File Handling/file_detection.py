# Pyhton file detection

import os

file_path = "File Handling/test.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a folder")
else:
    print("location does not exist")