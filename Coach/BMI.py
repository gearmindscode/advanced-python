# Lab 1 Part 4: Body Mass Index Calculator
# Date: 1/23/2025
# Name: Seth Hutchinson
a=float(input('Please input your weight in pounds: '))
b=float(input('Please input your height in inches: '))
print('')
BMI=(a/b**2)*703
print(f'Your BMI figure is {BMI:.2f}')
if BMI <=18.5:
    print('You are underweight')

elif BMI <=25:
    print('You are a healthy weight')

elif BMI <=30:
    print('You are overweight')

else:
    print('You are obese')
