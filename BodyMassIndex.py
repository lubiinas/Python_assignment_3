'''Write a program to calculate your BMI and give weight status. Body Mass Index (BMI) is an internationally used measurement to check if you are a healthy weight for your height.The metric BMI formula accepts weight in kilograms and height in meters:
BMI= weight(kg)/height2(m2)
BMI Weight Status Categories table
BMI range - kg/m2       Category
Below 18.5              Underweight
18.5 -24.9              Normal
25 - 29.9               Overweight
30 & Above              Obese'''
weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))
if height > 0:
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("You are in the 'Underweight' range.")
    elif 18.5 <= bmi <= 24.9:
        print("You are in the 'Normal' range.")
    elif 25 <= bmi <= 29.9:
        print("You are in the 'Overweight' range.")
    else:
        print("You are in the 'Obese' range.")
