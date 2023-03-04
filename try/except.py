 try:
     answer=10/0
    number=int(input("enter a no: "))
     print(number)
 except ZeroDivisionError as err:#err is a variable
     print(err)
 except ValueError:
    print("invalid input")

try:
    var=int(input("enter a no: "))
    print(var)
except:
    print("invalid")