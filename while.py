# Write a while loop that prints numbers from 1 to 5.

while i < 6:
  print(i)
  i+=1

# Write a while loop that prints "Hello, World!" 5 times.

i = 1
while i < 6:
  print("Hello, World!")
  i+=1

# Write a while loop that takes an integer input from the user and keeps asking until the user enters 0. When 0 is entered, print "Loop stopped".

integer = int(input("Enter a number: "))

while integer != 0:  # Keep looping until user enters 0
    integer = int(input("Enter the number again: "))

print("Loop stopped")

# Write a while loop to print all even numbers from 2 to 20.

even = 2
while even <=20:
  print(even)
  even+=2

# Write a while loop to calculate the sum of numbers from 1 to 10.

sum = 0
i = 1
while i <=10:
  sum+=i
  i+=1
print("Total sum: ", sum)

# Write a while loop to count backward from 10 to 1.

counter = 10
while counter >=1:
  print(counter)
  counter-=1
  
# Write a while loop to print the multiplication table of 5 (from 5×1 up to 5×10).

i = 1
num = 5
while i <=10: 

  print(num, "*" ,i,"=", num*i)
  i+=1

'''Write a while loop that asks the user to enter a password.
Keep asking until the user enters "python123".
When correct, print "Access Granted".'''

pass_word = input("Enter the password: ")
password = "python123"
while pass_word!= password:
  pass_word = input("Enter the password again: ")
print("Access Granted.")


'''Write a while loop that prints numbers from 1 to 50,
but skips numbers divisible by 3.'''

number = 1

while number <= 50:
    if number % 3 == 0:   # Skip numbers divisible by 3
        number += 1       # Move to the next number
        continue
    print(number)
    number += 1

