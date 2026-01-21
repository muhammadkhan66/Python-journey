# # Increasing Triangle

pattern_1 = 5
for i in range(pattern_1):
    for j in range(i+1):
        print("*", end="  ")
    print()

# # Decreasing Triangle

pattern_2 = 5
for i in range(pattern_2):
    for j in range(i,pattern_2):
        print("*", end=" ")
    print()

# # Right Angle Triangle

pattern_3 = 5
for i in range(pattern_3):
    for j in range(i,pattern_3):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

# # Right Sided Triangle

pattern_4 = 5
for i in range(pattern_4):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,pattern_4):
        print("*", end=" ")
    print()

# # Hill Pattern

pattern_5 = 5
for i in range(pattern_5):
    for j in range(i,pattern_5):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

# # Reverse Hill Pattern

pattern_6 = 5

for i in range(pattern_6):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,pattern_6-1):
        print("*", end=" ")
    for j in range(i,pattern_6):
        print("*", end=" ")
    print() 

# # Diamond Pattern

pattern_7 = 5
for i in range(pattern_7-1):
    for j in range(i,pattern_7):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(pattern_7):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,pattern_7-1):
        print("*", end=" ")
    for j in range(i,pattern_7):
        print("*", end=" ")
    print() 



