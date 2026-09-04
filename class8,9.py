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
"""file=open("students.txt","w")
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
file = open("students.txt", "r")
for line in file:
    print(line)  #on;y line means including whitespace its printed 
file.close() 

file = open("students.txt", "r")
for line in file:
    print(line.strip()) # stripe method removes any leading and whitespaces are removed 
file.close()


###CLASS 9
#mode- r w a r+ w+
#methods- open() read() write() close() seek() tell() 
#read methods: read() readline() readlines() 
#write methods:write() writelines() 
#difference between seek tell if no argument passed to tell then what would be default after write- last character, then wt if file opened in read method then what is default initial object pointer position  of file - very 1st character  
#from current pointer if u give arguments to tell (if u call tht method in display)

#different methods to inspect file properties
file=open("students.txt","r+")
readcontent = file.read()
file.write("\nThank you.")
print("read content :\n,readcontent")
print( "file mode:",file.mode)
print( "file name:",file.name)
print( "file close:",file.closed)"""

#with statement - no close method but file could be closed
# with open("students.txt","a")as file:
#     name=input("enter new student name:")
#     file.write(name+ "\n")
# print("student added successfully")
# print("file closed",file.closed)

#counting lines,words,and characters in a file(do this without builtin - hw)
# with open("students.txt","r") as file:
#     content = file.read()
# lines = content.splitlines()
# words = content.split()
# character = len(content)
# print("number of lines:",len(lines))
# print("number of words:",len(words))
# print("number of characters:",character)

#the file pointer tell
with open("students.txt","r") as file:
    print("initial position:",file.tell())
    print(file.read(5))
    print("position after reading:",file.tell())


with open("students.txt","r") as file:
    print(file.read(10)) # other wise default starts from 0
    print("initial position before seeking:",file.tell())
    file.seek(5) #including white space
    print("position after seeking:",file.tell())
    print(file.read(6)) # from 5 to 6 character

#scenario:
# an MCA department wants to store student information such as:
# tasks:
# write the info to the file
# read that 5 students information
# search for particular student information
# change 1st year to promote to 2nd year for students - save as file from 1st yr to 2nd yr , trying to rename or copying opriginal file and try to create backup file 
# how would u delete a file - using method remove (how would u call a method call remove - by importing os.remove(filename) for folder how would u delete ? - rmdir)
#


