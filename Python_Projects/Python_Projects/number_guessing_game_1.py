#First we are importing random. It is a module which would help us in generating a random number
import random
# We have welcomed the user to our game
print("Welcome to the Number Guessing Game")
# We have informed the user about the numbers between 1 to 100 and they have to guess from it
print("I am thinking about a number between 1-100. You have to guess it")
ready = input("Are you ready ? Type Y/N ")
print("You have total of 10 attempts")

#Now, we are generating a random number and storing it in a variable
secret_number = random.randint(1,100)
#We have created a variable named attempt to store the number of attempts
attempt = 0
# We have created an infinite loop and asked the user to enter the number.
while True:
    #This variable stores the value of the guess of the user
    guess = input("Enter a number: ")
    # This checks whether the input from the user is a digit or not. If not it throughs an error.
    if not guess.isdigit():
        print("Enter a valid input.")
        # The continue statement again gets the input from the user if user enters an invalid input
        continue
    #This increments the attempt by one number.
    attempt +=1
    #This if statement checks whether attempt has reached 10 digits or not. If 10 is reached, than it prints the attempts are over.
    if attempt == 10:
        print("You'r attempts are over!")
        break
    #This converts the guess input to int
    guess = int(guess)
    #This condition  compares the guess number with the secret number. If guess is greater than the secret number it prints too high.
    if guess>secret_number:
        print("Too High! Try again")
        #If guess is less than the secret number, than it prints too low.
    elif guess<secret_number:
        print("Too low! Try again")
        #If the user gets the guess correct, than it prints a congrats message.
    else:
        print(f"Congrats ! You have guessed the number in {attempt} attempts")
        print("Game Over!")