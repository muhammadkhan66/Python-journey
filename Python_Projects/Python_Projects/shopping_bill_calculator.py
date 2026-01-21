# Initialize sum variable to store the total bill amount
sum = 0

# Start an infinite loop to keep asking for item prices
while True:
    # Ask the user to enter an item price or press 'q' to quit
    item_price = input("Enter the price or press q to quit: ")

    # Check if the user did NOT enter 'q'
    if item_price != "q":
        # Convert the entered price to integer and add it to sum
        sum = sum + int(item_price)

        # Display the total bill so far
        print(f"Total bill so far: {sum} ")
    else:
        # If user enters 'q', print the final bill
        print(f"Your total bill is {sum}. Thanks for shopping with us.")

        # Exit the loop
        break
