#File handling with Exception handling

#open file and read it and also use exception handling

import csv

fields=[]
rows=[]

filename="data.csv"
try:
    with open(filename,"r")as csvfile:
        csvreader=csv.reader(csvfile)

        fields=next(csvreader)

        for row in csvreader:
            rows.append(row)
except FileNotFoundError:
    print("File does not exist")

except Exception as e:
    print("Error")

total_marks=0
number=0

for row in rows:
    total_marks+=int(row[1])
    number+=1
notes=[]
for row in rows:
    if (row[2]=="A"):
        notes.append("Good")
    elif(row[2]=="B"):
        notes.append("Not Bad")
    elif(row[2]=="C"): 
        notes.append("Study hard") 

avg_marks=total_marks//number


#writing data
try:
    with open("result.txt", "w",newline='') as csvfile:
        csvwriter=csv.writer(csvfile)#To write into scv file

        csvwriter.writerow(["Average","total marks","Note"])
        csvwriter.writerow([avg_marks,total_marks,notes])


except Exception as ep:
    print("Result file not created")

#Not a perfect code , but it's okay 