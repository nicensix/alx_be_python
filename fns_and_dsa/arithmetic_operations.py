def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Type of arithmetic operation ('add', 'subtract', 'multiply', 'divide')

    Returns:
        float or str: Result of the arithmetic operation or an error message for division by zero
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation. Choose from 'add', 'subtract', 'multiply', or 'divide'."