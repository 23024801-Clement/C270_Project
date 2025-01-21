def calculate(num1, num2, operation):
    # Validate inputs
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "Please enter valid numbers."
    
    # Perform calculation based on operation
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero."
        return num1 / num2
    else:
        return "Invalid operation."
