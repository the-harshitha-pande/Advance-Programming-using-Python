#file handling
#what is file? why do we need to handle files?list different types of file.
#text file-txt,json,xml,document,
#modes of file- read,write,
#operations - open(also called as method),close,
#ovwrites information- when file opened n write 
#readlines writeline read write not only modes ty are also operations

#filehandling-textfile : fundamentals
#read r #write w #readwrite r+ #append a, writeread w+
#without file pointer how would u close without file.close - its "with" operation . why is with recommended
#to close operation - file.close

#file object-


#create/open a file
file=open("students.txt","w")
print("file opened successfully")
file.close

#writing to a existing text file
file=open("students.txt","w")
file.write("Anita\n") #tring to write the data with help of write method
file.write("Rahul\n")
file.write("priya\n")
file.close
print("students details saved successfully")

#writing multiple lines with help of writelines() - with help of list
students=["Anita\n","Rahul\n","kiyara\n"] #this has overwritten existing information - always write overwrites the info not append
file=open("students.txt","w")
file.writelines(students)
file.close

#appending 
students=["maira\n","kuhu\n"]
file=open("students.txt","a")
file.writelines(students)# the write method is also sufficient for appending information
file.close

#reading a complete file
file=open("students.txt","r")
content=file.read()
print(content)
file.close()

#reading a specific number of character
file=open("students.txt", "r")
content=file.read(10) #the read(n) method reads n character
print(content)
file.close

#reading one line at a time
file=open("students.txt", "r")
line=file.readline() #readlines() returns a list of string insted of readline()
print(line)
file.close()
#reading a file using for loop - hw