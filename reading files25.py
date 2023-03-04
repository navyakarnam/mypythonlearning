stud_file= open("stud.txt","r")#w,a,r+(read and write)
print(stud_file.readable())    #file can be read as it gives true
#print(stud_file.read())       #all the information in the stud_file is printed
#print(stud_file.readline())   #reads and prints the individual lines in the file
#print(stud_file.readlines())  #it puts it inside an array or list and prints the entire file
#print(stud_file.readlines()[0]) #returns the element in the zeroth position

for student in stud_file.readlines():
    print(student)
stud_file.close()