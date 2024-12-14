# # factorial
num=int(input("enter the number"))
fact=1
if num>=0:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of the num is",fact)
else:
    print("factorial is not defined for negative number")
# reverse
num_1 = int(input("Enter a number to reverse: "))
reversed_num = 0
while num_1 > 0:
    digit = num_1 % 10
    reversed_num = reversed_num * 10 + digit
    num_1//= 10
print(f"The reversed number is:{reversed_num}")
# Multiples of a Number
num_2=int(input("Enter a number"))
i=1
while i<11:
    print(i,"*",num_2,"=",num_2*i)
    i+=1
# Write a program to print the inputted value as it is and break the loop if the value is 'done'.
while True:
    value = input(":")
    print(value)
    if value.lower() == 'done':
        break
# Write a program that prints the numbers from 1 to 10. But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
for i in range(1,11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
# Pattern Printing
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()






