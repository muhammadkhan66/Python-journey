#Question 1
try:
    num = int(input("Enter a number: "))
    print(f'Square of the number is: {num * num}')
except ValueError:
    print('Enter a valid number.')


#Question 2
try:
    number = [34, 56, 78, 90]
    index = int(input("Enter an index: "))
    print(number[index])
except (IndexError):
    print("Index out of range. Enter a valid index.")
except ValueError:
    print("Please enter numbers only.")
#Question 3

while True:
    try:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        print(f"Division of num1 and num2 is: {num1/num2} ")

    except ZeroDivisionError:
        print("Do not divide by zero.")

#Question 4

try:
    a = open("harry.txt", "r")
    content = a.read()
    print(content)
    a.close()
except FileNotFoundError:
    print("File not found. Enter a valid file.")

#Question 5

try:
    number =  input("Enter a number: ")
    int_num = int(number)
    print(f"You entered: {int_num}")
except (ValueError, TypeError):
    print("Invalid Input! Enter a valid number.")

# Question 6

numbers = [12,34,56,8,0]

for num in numbers:
    try:
        reciprocal = 1 / num
        print(f"Reciprocal of {num} is {reciprocal}")
    except ZeroDivisionError:
        print(f"Division of reciprocal of {num} with 0 is not possible.")
#Question 7

numberrs = [34,12,9,8,"Khan",34,84]
total = 0
for num in numberrs:
    try:
        total+= int(num)
    except (ValueError,TypeError):
        print("Invalid data type: ",  num)
print("Sum of valid numbers: ", total)



