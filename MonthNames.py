# Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.
number_month=int(input("enter a number between 1&12"))
month=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
if 1 <= number_month <= 12:
    print("month" ,number_month, "is",month[number_month-1])
else:
    print("invalid month,please enter number between 1&2")
#A certain cinema currently sells tickets for a full price of 6 pounds, but always sells tickets for half price to people who are less than 16 years old, and for a third of the price for people who are 60 years old or more.
age=int(input("Enter your age"))
full_price = 6
ticket_price = full_price
if age < 16:
    ticket_price = full_price / 2
elif age >= 60:
    ticket_price = full_price / 3
print(f"Your ticket costs £{ticket_price:.2f}")
#

