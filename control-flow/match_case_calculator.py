# This code does simple arithmetic calculations

num1 = float(input("Enter the first number: "))  # prompts user to enter the first number
num2 = float(input("Enter the second number: "))  # prompts user to enter the second number
operation = (input("Choose the operation (+, -, *, /): "))  # prompts user to choose arithmetic operation to carry out

match operation:
    case "+" :
        result = num1 + num2
        print("The result is", result, ".")
    case "-" :
        result = num1 - num2
        print("The result is", result, ".")
    case "*" :
        result = num1 * num2
        print("The result is", result, ".")
    case "/" :
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print("The result is", result, ".")