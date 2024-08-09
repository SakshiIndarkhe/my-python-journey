#File handling with Exception handling

#open file and rread it and also use exception handling
#i will complete it afterwards
import csv
f=open("data.csv" ,"r")
if (f==0):
    print("No file found")

field=[]
rows=[]


csvreader=csv.reader(f)

field=next(csvreader)

for row in csvreader:
    rows.append(row)

print(field)
print(rows)

f.close()