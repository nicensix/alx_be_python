num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is: {result}")
    case '-':
        result = num1 - num2
        print(f"The result is: {result}")
    case '*':
        result = num1 * num2
        print(f"The result is: {result}")
    case '/':
        if num2 == 0:
            print("Cannot divide by zeoro.")
        else:
            result = num1 / num2
            print(f"The result is: {result}")
    case _:
        result = "Error: Invalid operation. Please choose from +, -, *, or /."