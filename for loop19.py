#for loops are used to loop over a collection of items such as strings, arrays and numbers.

#for loop in strings
for letter in "Bhavya":
    print(letter)#here the variable letter is going to iterate through every letter in the word,
    # for each letter in bhavya print that individual letter

#arrays
Family=["Bhavya","Navya","Divya"]
for sisters in Family:#sisters is just a random variable
    print(sisters)

#numbers
for no in range(20):#it excludes the last no
    print(no)

for index in range(0,10):
    print(index)

Names=["jim","kim","carry"]#second way of printing
for variable in range(len(Names)):#Names[0]
    print(Names[variable])        #Names[1]
                                  #Names[2]

for variable in range(5):
    if variable==0:
        print("hey its the first iteration")
    else:
        print("oops, not first yaara")#rest 4