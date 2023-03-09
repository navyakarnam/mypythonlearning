#To find the sum and average of a no entered by the user

sum=0
nocount=0

while True:      #infinite loop
    number = int(input("Enter the no: "))
    sum=sum+number
    nocount=nocount+1

    choice=input("Do you want to enter the no, type (y/n): ")
    if choice.casefold()=='n':
        break

print(f"sums: {sum}")        #f stands for format
average=sum/nocount
print(f"average: {average}")
