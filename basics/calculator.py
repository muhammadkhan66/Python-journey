try: 

    number_1 = int(input("Enter the first number: "))

    number_2 = int(input("Enter the second number: "))

    print("What operation do you want to perform ? Press + for  addition\n Press - for subtraction\n Press * for multiplication\n Press / for division.")

    operation =  input(" Enter the operation: ")
    match operation:
        case "+":
            print(f"The  result is: {number_1 + number_2}")
        case "-":
            print(f"The result is: {number_1 - number_2}")
        case "*":
            print(f"The result is: {number_1 * number_2}")
        case "/":
            print(f"The result is:  {number_1/number_2}")

except Exception as e:
    print(" Enter a valid  value for  number_1 and number_2 ")




