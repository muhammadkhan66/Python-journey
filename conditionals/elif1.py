# Question 1

'''Write a Python program that takes an integer input from the user and checks:

If the number is positive and even, print "Positive and Even".

If the number is positive and odd, print "Positive and Odd".

If the number is zero, print "Zero".

Otherwise, print "Negative".'''

integer = int(input("'Enter a number : "))

if (integer>0 and integer%2==0):
    print(f"{integer} is positive and even number.")
elif (integer>1 and integer%2!=0):
    print(f"{integer} is positive and odd number.")
elif(integer==0):
    print(f"{integer} is a zero.")
else:
    print(f"{integer} is negative.")

# Question 2

'''A store gives discounts based on purchase amount:

If the bill is ≥ 5000, give 20% discount

If the bill is ≥ 3000 and < 5000, give 10% discount

If the bill is ≥ 1000 and < 3000, give 5% discount

Otherwise, no discount

Write a Python program to input the bill amount and display the discounted price.'''

bill_amount = int(input("Enter the bill amount: "))

if (bill_amount>=5000):
    discount = bill_amount*0.20
    final_amount = bill_amount-discount
    print(f"Congrats! you got a 20% discount of {discount}.Final amount is {final_amount}")
elif(3000<=bill_amount<5000):
    discount = bill_amount*0.10
    final_amount = bill_amount-discount
    print(f"Congrats! you got a 10% discount of {discount}.Final amount is {final_amount}")
elif(1000<=bill_amount<3000):
    discount = bill_amount*0.05
    final_amount = bill_amount-discount
    print(f"Congrats! you got a 5% discount of {discount}. Final amount is {final_amount}")
else:
    print("Sorry, you got no discount.")

# Question 3

a= int(input("Enter number 1: "))
b= int(input("Enter number 2: "))
c= int(input("Enter number 3: "))

if a>=b:
    if a >=c:
        print(f"{a} is the greatest number.")
    else:
        print(f"{c} is the greatest.")
if b>=c:
    print(f"{b} is the greatest number.")

else:
    print(f"{c} is the greatest.")

# Question 4

'''A company wants to calculate an employee’s bonus based on the following conditions:

If experience ≥ 5 years and salary ≥ 50,000 → Bonus = 10% of salary

If experience ≥ 5 years and salary < 50,000 → Bonus = 7% of salary

If experience < 5 years → Bonus = 5% of salary

Write the program to calculate and display the bonus.'''

experience =int(input("Enter your experience: "))
salary = float(input("Enter your salary: "))

if (experience >=5 and salary>=50000):
    bonus = salary*0.10
    final_salary = bonus + salary
    print(f"Your salary with 10 percent bonus is {bonus}. Final salary is {final_salary}")
elif(experience >=5 and salary < 50000):
    bonus = salary * 0.07
    final_salary = bonus + salary
    print(f"Your salary with 7 percent bonus is {bonus}. Final salary is {final_salary}")

elif(experience < 5 ):
    bonus = salary*0.05
    final_salary = bonus + salary
    print(f"Your salary with 5 percent bonus is {bonus}. Final salary is {final_salary}")

# Question 5

'''Write a Python program to check if a given year is a century leap year or not.
A year is a leap year only if:

It is divisible by 400, or

It is divisible by 4 and not divisible by 100.'''

leap_year = int(input("Enter the year:"))

if leap_year%400==0:
    print(f"{leap_year} is a leap year.")

elif(leap_year%4==0 and leap_year%100!=0):
    print(f"{leap_year} is a leap year.")
else:
    print(f"{leap_year} is not a leap year.")


# Question 6

'''Write a Python program that takes a student’s marks as input and prints the grade based on the following:

90 and above → "A+"

80 to 89 → "A"

70 to 79 → "B"

60 to 69 → "C"

50 to 59 → "D"

Below 50 → "Fail"'''

marks = int(input("Enter your marks: "))

if marks>=90:
    print("A+")
elif 80<=marks<=89:
    print("A")
elif 70<=marks<=79:
    print("B")
elif 60<=marks<=69:
    print("C")
elif 50<=marks<=59:
    print("D")
else:
    print("Fail")

# Question 7

'''A movie theater charges ticket prices based on age:

Below 5 years → Free

5 to 12 years → 50% discount

13 to 59 years → Full price

60 years and above → 30% discount

Assume the base ticket price is 500 PKR.
Write a Python program to calculate and print the final ticket price.'''

ticket_price = 500
age = int(input("Please enter your age: "))

if age<5:
    ticket_price *=0
    print(f"Free. your ticket price is {ticket_price}")
elif 5<=age<=12:
    ticket_price*=0.5
    print(f"You got a 50% discount. your ticket price is {ticket_price}")
elif 13<=age<=59:
    ticket_price = 500
    print(f"your ticket price is{ticket_price}")
elif age>=60:
    ticket_price*=0.7
    print(f"You got a 30 % discount. Your ticket price is{ticket_price}")

# Question 8

'''Write a Python program that takes a character from the user and checks:

If it is a vowel, print "Vowel"

If it is an alphabet but not a vowel, print "Consonant"

Otherwise, print "Not an alphabet".'''

alpha = input("Enter an alphabet: ")

if alpha in('AEIOUaeiou'):

    print(f"{alpha} is a vowel.")

elif alpha not in ("AEIOUaeiou"):

    print(f"{alpha} is a consonant.")
else:
    print("Not an alphabet.")


# Question 9

username = input("Enter the username: ")
password = input("Enter the password:")

correct_username = 'username'
correct_password = '1234'


if(username==correct_username) and(password==correct_password):
    print("Login successfully.")
elif(username==correct_username) and (password!=correct_password):
    print("Incorrect password.")
elif(username!=correct_username) and (password==correct_password):
    print("Incorrect username.")
else:
    print("Invalid login.")

    # Question 10

num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))
num3 = int(input("Enter the number 3 : "))

if num1==num2==num3: 
    print("All numbers are equal.")
elif(num1==num2) and (num1>num3):
    print(f"{num1} and {num2} are  both equal and greater than {num3}")
else:
    greatest = max(num1,num2,num3)
    print(f"{greatest} is the greatest number.")


