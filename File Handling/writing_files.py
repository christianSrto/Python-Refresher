# Python writing files (.txt, .json, .csv)

import json
import csv

employees = ["Mr. Krabs", "Spongebob", "Squidward"]

txt_data = "This works"

file_path = "File Handling/output.txt"

#other modes r = read, a = append, x = writes if that file doesn't exist
with open(file=file_path, mode="w") as file:
    for employee in employees:
        file.write(employee + "\n")
    print("file was created")

try:
    with open(file=file_path, mode="a") as file:
        file.write("\n" + txt_data)
        print("file was created")
except FileExistsError:
    print("that file already exists")

try:
    with open(file=file_path, mode="x") as file:
        file.write("using x mode")
        print("file was created")
except FileExistsError:
    print("that file already exists")



#json file handling

json_path = "File Handling/output.json"

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

with open(file=json_path, mode="w") as file:
    json.dump(employee, file, indent=4)
    print("json file was created")



#csv file handling 

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Mr. Krabs", 50, "Owner"],
             ["Squidward", 40, "Cashier"]]

csv_path = "File Handling/output.csv"

#new line = "" makes it so that employees is written without big gaps in output file 
with open(file=csv_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print("csv file was created")