# Increasing triangle pattern of 1

pattern_1 = 5
for i in range(pattern_1):
    for j in range(i+1):
        print("1", end=" ")
    print()

# Increasing triangle pattern of numbers

pattern_2 = 5
p = 1
for i in range(pattern_2):
    for j in range(i+1):
        print(p, end="")
    p+=1
    print()

# Decreasing triangle pattern of numbers

pattern_3 = 5
p = 5
for i in range(pattern_3):
    for j in range(i+1):
        print(p, end=" ")
    p-=1
    print()

# Increasing triangle of numbers with increment of 2

pattern_4 = 5
p = 0
for i in range(pattern_4):
    for j in range(i+1):
        print(p, end=" ")
    p+=2
    print()

# Printing two different numbers using if else

pattern_5 = 5

for i in range(pattern_5):
    for j in range(i+1):
        if i % 2 == 0:
            print("1", end=" ")
        else:
            print("2", end=" ")
    
    print()

# Printing two different alphabets using if else

pattern_6 = 5

for i in range(pattern_6):
    for j in range(i+1):
        if i % 2 == 0:
            print("A", end=" ")
        else:
            print("B", end=" ")
    print()

# Decreasing triangle pattern of two different numbers

pattern_7 = 5

for i in range(pattern_7):
    for j in range(i,pattern_7):
        if i % 2 == 0:
            print("1", end=" ") 
        else:
            print("3", end=" ")
    print()

# Decreasing triangle of two different characters

pattern_8 = 5
for i in range(pattern_8):
    for j in range(i,pattern_8):
        if i % 2 == 0: 
            print("#", end=" ")
        else:
            print("$", end= " ")
    print()

# Hill Pattern using two different characters

pattern_8 = 5
for i in range(pattern_8):
    for j in range(i,pattern_8):
            
            print(" ", end=" ")
    for j in range(i+1):
            if i % 2 == 0:
                   
                print("#", end= " ")
            else:
                  print("$", end=" ")
    for j in range(i):
            if i % 2 == 0:
                   
                print("#", end= " ")
            else:
                  print("$", end=" ")
    print()
