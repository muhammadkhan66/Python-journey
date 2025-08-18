# Question 1
# What will be the output of the following code and why?
a = 10
b = 20
c = a < b and b > 15
print(c)

Output =  True

# Question 2
# Explain the difference between is and == operators in Python with an example.

# == → checks value equality

# is → checks object identity (memory location)

# Question 3
# Predict the output:
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

# output  
# True
# False

# Question 4

# What does the expression 5 & 3 return in Python, and why?
d = 5 & 3
print(d)
# returns 1.

# Here’s why (bitwise AND works on binary form):

# 5 in binary → 0101

# 3 in binary → 0011

# Question 5

num = 7
print(num >> 1)
print(num << 2)

# Step 1: Convert 7 to binary

7 in binary = 0111

# Step 2: Right shift (>> 1)

# num >> 1 means shift all bits one place to the right.

# 0111 (7 in binary)
# ↓ shift right by 1
# 0011 (which is 3 in decimal)


# So num >> 1 = 3

# Step 3: Left shift (<< 2)

# num << 2 means shift all bits two places to the left.

# 0111 (7 in binary)
# ↓ shift left by 2
# 11100 (which is 28 in decimal)


#  So num << 2 = 28
