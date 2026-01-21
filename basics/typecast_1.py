# Typecasting in Python - Questions and Answers


# ------------------
# Q1: What is typecasting in Python, and what are the two types of typecasting?
# # Answer in concept, no code needed.

# Q2: Convert the string "25" into an integer and add 10 to it.
string = "25"
print(int(string) + 10)   # Output: 35

# Q3: Convert float 12.7 into int.
num = 12.7
print(int(num))   # Output: 12

# Q4: Convert integer 5 into a string and concatenate with " apples".
number = 5
print(str(number) + " apples")   # Output: 5 apples


# MEDIUM (4 Questions)
# --------------------
# Q5: Convert string "3.5" into float and multiply by 2.
a = "3.5"
b = float(a)
print(b * 2)   # Output: 7.0

# Q6: Why error with int("abc")? Show fix with numeric string.
# # Error example
x = "abc"
y = int(x)   # ValueError
# Fix example
x = "3.5"
y = int(float(x))
print(y)   # Output: 3

# Q7: Convert ["10", "20", "30"] into list of integers.
data = ["10", "20", "30"]
data1 = [int(i) for i in data]
print(data1)   # Output: [10, 20, 30]

# Q8: Convert int to str and concatenate.
value = 7
print(str(value) + "7")   # Output: "77"


# EXTREME DIFFICULT (2 Questions)
# -------------------------------
# Q9: Convert ["10", "20.5", 30, "40"] into list of floats.
data = ["10", "20.5", 30, "40"]
data1 = [float(i) for i in data]
print(data1)   # Output: [10.0, 20.5, 30.0, 40.0]

# Q10: Difference between float("inf") and int("inf").
print(float("inf"))   # Output: inf
print(int("inf"))   # ValueError: invalid literal for int() with base 10: 'inf'
