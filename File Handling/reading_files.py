# Python reading files (.txt, .json, .csv)
import json
import csv

#txt file reading
print("\ntxt file:")
file_path = "File Handling/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
#for files that are write-only or permission to read is not granted
except PermissionError:
    print("You do not have permission to read that file")



#json file reading
print("\njson file:")
json_path = "File Handling/output.json"

try:
    with open(json_path, "r") as file:
        content = json.load(file)
        #can access content by key
        print(content["name"])
except FileNotFoundError:
    print("That file was not found")
#for files that are write-only or permission to read is not granted
except PermissionError:
    print("You do not have permission to read that file")



#csv file reading
print("\ncsv file:")
csv_path = "File Handling/output.csv"

try:
    with open(csv_path, "r") as file:
        content = csv.reader(file)
        #prints memory address
        print(content)

        for line in content:
            #prints specific column from the csv file
            print(line[1])
except FileNotFoundError:
    print("That file was not found")
#for files that are write-only or permission to read is not granted
except PermissionError:
    print("You do not have permission to read that file")
