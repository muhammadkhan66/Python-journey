# Question 1
'''Write a program to check whether a number is positive, negative, or zero.'''
num =  int(input("Enter a number: "))

if num>0:
    print(f"{num} is a positive number.")
elif num<0:
    print(f"{num} is a negative number.")
else:
    print(f"{num} is a zero.")

# Question 2

'''Write a program to determine if a year is a leap year or not.'''

year = int(input("Enter a year: "))

if(year%400==0) or(year%4==0 and year%100!=0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Question 3

'''Write a program that takes three numbers as input and prints the largest one.'''

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num3<=num1>=num2:
    print(f"{num1} is the greatest number.")
elif num1<=num2>=num3:
    print(f"{num2} is the greatest number.")
else:
    print(f"{num3} is the greatest number.")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

# 2nd Method using max function
greatest = max(num1,num2,num3)
print(f"The greatest number is {greatest}")

# Question 4

'''Write a program that checks whether a given character is a vowel or consonant.'''

alpha = input("Enter an alphabet:  ")

if (alpha in "AEIOUaeiou"):
    print(f"{alpha} is a vowel.")
else:
    print(f"{alpha} is a consonant.")

# Question 5

'''Write a program to check if a number is even and divisible by 5, even but not divisible by 5, or odd.'''

number = int(input("Enter a number: "))

if (number%2==0 and number%5==0):
    print(f"{number} is an even number and divisible by 5.")
elif (number%2==0 and number%5!=0):
    print(f"{number} is an even number but not divisible by 5.")
elif(number%2!=0):
    print(f"{number} is odd number.")

# Question 6

'''Write a program that asks for a user’s age and prints:

“Child” if age < 13

“Teenager” if 13 ≤ age < 20

“Adult” if 20 ≤ age < 60

“Senior” if age ≥ 60'''

age = int(input("Enter your age: "))

if age<13:
    print("Child")
elif 13<=age<20:
    print("Teenager")
elif 20<=age < 60:
    print("Adult")
elif age>=60:
    print("Senior")


# Question 7

'''Write a program that takes marks (0–100) as input and prints the grade according to this scale:

90–100 → A

80–89 → B

70–79 → C

60–69 → D

Below 60 → F'''

marks = int(input("Enter your marks: "))

if marks>=90:
    print("A")
elif 80<=marks<=89:
    print("B")
elif 70<=marks<=79:
    print("C")
elif 60<=marks<=69:
    print("D")
elif marks<60:
    print("F")

# Question 8

'''Write a program that checks if a number is prime or not (use if-else without importing libraries).'''

prime_number = int(input("Enter a number: "))

if prime_number<=1:
    print("Enter a valid number.")
if prime_number>1:
    for i in range(2,prime_number):
        if prime_number%i==0:
            print(f"{prime_number} is not a prime number.")
            break
    else:
        print(f"{prime_number} is a prime number.")


# Question 9

'''  Write a program that takes the lengths of three sides and determines whether they form a valid triangle. (Hint: sum of any two sides must be greater than the third.)'''

a = int(input("Enter length 1: "))
b = int(input("Enter length 2: "))
c = int(input("Enter length 3: "))

if (a+b>c) and (b+c>a) and (a+c>b):
    print("It is a valid triangle.")
else:
    print("It is not a valid triangel.")

# Question 10

'''Write a program that takes an integer and checks if it is:

A multiple of both 3 and 7

A multiple of only 3

A multiple of only 7

Not a multiple of either'''

multiple = int(input("Enter a number: "))

if multiple % 3 == 0 and multiple % 7 == 0:
    print(f"{multiple} is a multiple of both 3 and 7.")
elif multiple % 3 == 0:
    print(f"{multiple} is a multiple of 3 only.")
elif multiple % 7 == 0:
        print(f"{multiple} is a multiple of 7 only.")
else:
     print(f"{multiple} is a multiple of neither.")
