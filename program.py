#1. Write a Python program to convert kilometers to miles?


kilometer = float(input("Enter the value of kilometer :  "))
conversion_factor = 0.621371
miles = kilometer * conversion_factor
print('%0.2f kilometers is equal to %0.2f miles' %(kilometer,miles))


#2. Write a Python program to convert Celsius to Fahrenheit?

celsius = float(input("enter the tempreture value in celsius:  "))
multiplied_factor = 1.8
Fahrenheit = (celsius * multiplied_factor) + 32
print('%0.2f celsius is equal to %0.2f fahrenheit' %(celsius,Fahrenheit))


#3. Write a Python program to display calendar?

import calendar

yy = int(input("Enter year : "))
mm = int(input("Enter month : "))

print(calendar.month(yy, mm))


#4. Write a Python program to solve quadratic equation?

import cmath

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d = (b**2) - (4*a*c)
solution1 = (-b-cmath.sqrt(d))/(2*a)
solution2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(solution1,solution2))


#5. Write a Python program to swap two variables without temp variable?

x = 10
y = 5

x = x + y

y = x - y
x = x - y
print("After Swapping: x =", x," y =", y)