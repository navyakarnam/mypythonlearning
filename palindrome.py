#To find whether the entered no is palindrome or not

print("Enter the number")
number=int(input())
temp=number
reverse=0

while(number>0):
    dig=number%10
    reverse=reverse*10+dig
    number=number//10  #floor or integer division

if temp==reverse:
    print("The no is a palindrome")
else:
    print("Not a palindrome")
