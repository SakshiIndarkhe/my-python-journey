#File handling
f=open("demofile.txt","w+") #for writing and reading

# open function takes two parameter file name and mode

f.write("THis is text file")

f.seek(0)

print(f.readline())

f.close()
