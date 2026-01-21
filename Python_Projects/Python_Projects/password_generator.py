# Import string module to get predefined character sets
import string

# Import random module for shuffling characters
import random

# Store different types of characters
s1 = string.ascii_letters      # All letters (a-z, A-Z)
s2 = string.ascii_lowercase    # Lowercase letters (a-z)
s3 = string.ascii_uppercase    # Uppercase letters (A-Z)
s4 = string.punctuation        # Special characters (!, @, #, etc.)
s5 = string.digits             # Numbers (0-9)

# Take password length input from user and convert it to integer
plen = int(input("Enter the password length: "))

# Create an empty list to store all characters
s = []

# Add all character sets to the list
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
s.extend(s5)

# Shuffle the characters randomly
random.shuffle(s)

# Generate and print the password of required length
print("".join(s[0:plen]))
