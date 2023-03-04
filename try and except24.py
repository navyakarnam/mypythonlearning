#it handles errors instead of throwing errors
try:
    #value=10/0
    number=int(input("Enter a number: "))
    print(number)

except ZeroDivisionError:
    print("Can't be divided by 0")

except ValueError:
    print("invalid input")