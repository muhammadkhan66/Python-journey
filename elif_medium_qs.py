


# # Question 11
marks = int(input("Enter the marks 0-100: "))

if 90<=marks<=100:
    print("A")
elif 80<=marks<=89:
    print("B")
elif 70<=marks<=79:
    print("C")
elif 60<=marks<=69:
    print("D")
else:
    print("F")

# # Question 12



number1 = int(input("Enter 1st number\n"))
number2 = int(input("Enter 2nd number\n"))
number3 = int(input("Enter 3rd number\n"))

# 1. Check if all numbers are equal
if number1 == number2 == number3:
    print("All numbers are equal.")

# 2. Check if exactly two numbers are equal
elif number1 == number2 != number3:
    print("1st and 2nd numbers are equal.")
    print("The greatest number is:", number1)

elif number1 == number3 != number2:
    print("1st and 3rd numbers are equal.")
    print("The greatest number is:", number1)

elif number2 == number3 != number1:
    print("2nd and 3rd numbers are equal.")
    print("The greatest number is:", number2)

# 3. If no equal numbers, check which is greatest
elif number1 > number2 and number1 > number3:
    print("1st number is the greatest.")

elif number2 > number1 and number2 > number3:
    print("2nd number is the greatest.")

elif number3 > number1 and number3 > number2:
    print("3rd number is the greatest.")

# # Questionn 13

year = int(input("Enter the year\n"))

if ( year % 400 == 0) or ( year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year.")

# # Question 14

username = input("Enter your username\n")
password = input("Enter your password\n")

if username == "admin" and password == "12345":
    print("login successfully")
else:
    print("Invalid credentials")

# # Question 15

traffic_light = input("Enter the traffic light colour\n")

if traffic_light == "red":
    print("Stop")
elif traffic_light == "yellow":
    print("slow down")
elif traffic_light == "green":
    print("Go")
else:
    print("Invalid colour.")

# # Question 16

total_shopping_amount = float(input("Enter the total shopping amount\n"))


if total_shopping_amount >= 5000:
    discount_price = total_shopping_amount * 0.20
    final_amount = total_shopping_amount - discount_price

    print("You got a 20 percent discount. Discounted price is: ", final_amount)
elif total_shopping_amount >= 3000:
    discount_price = total_shopping_amount * 0.15
    final_amount = total_shopping_amount - discount_price
    print("You got 15 percent discount. Discounted price is: ", final_amount)
elif total_shopping_amount >= 1000:
    discount_price = total_shopping_amount*0.10
    final_amount = total_shopping_amount - discount_price
    print("You got 10 percent discount. Discounted price is: ", final_amount)

else:
    print("There is no discount.")            

# # Question 17

character = input("Enter the character\n")

if len(character) != 1:
    print("Enter one character please")
else:

    if character.islower():
        print("Character is lowercase.")
    elif character.isupper():
        print("Character is uppercase.")
    elif character.isdigit():
        print("Characater is a digit.")
    else:
        print("It is a Special character.")

# # Question 18

num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))

operation = input("Enter the operator\n")

if operation == "+":
    result = num1 + num2
    print("Result: ", result)
elif operation == "*":
    result = num1 * num2
    print("Result: ", result)

elif operation == "-":
    result = num1 - num2
    print("Result: ", result)
elif operation == "/":
    result = num1 / num2
    print("Result: ", result)
    
# # Question 19

age = int(input("Enter your age\n"))
income = int(input("Enter your income\n"))

if 21<= age <= 60 and income >=30000:
    print("Eligible")
else:
    print("Not eligible")

# # Question 20

temp = float(input("Enter the temperature\n"))

if temp >=40:
    print("Very Hot")
elif 30<= temp <=39:
    print("Hot")
elif 20<= temp <= 29:
    print("Warm")
elif 10<=temp<=19:
    print("Cool")
elif temp <10:
    print("Cold")





        

