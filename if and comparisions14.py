num1 = float(input("Enter the first no: "))
num2 = float(input("Enter the sec no: "))
num3 = float(input("Enter the third no: "))


def max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:          # comparision operators are used
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num2 and num3 >= num1:
        return num3


# print((max(3,4,5))  calling the fn



def result():
    result = int(max(num1, num2, num3))
    print (str(result)+" is largest")

result()
