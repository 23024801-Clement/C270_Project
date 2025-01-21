function calculate() {
    // Get inputs and operation
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operation = document.getElementById('operation').value;

    // Validate inputs
    if (isNaN(num1) || isNaN(num2)) {
        document.getElementById('result').innerText = "Please enter valid numbers.";
        return;
    }

    // Prepare JSON data
    const data = {
        num1: num1,
        num2: num2,
        operation: operation
    };

    // Perform calculation based on the JSON data
    let result;
    switch (data.operation) {
        case 'add':
            result = data.num1 + data.num2;
            break;
        case 'subtract':
            result = data.num1 - data.num2;
            break;
        case 'multiply':
            result = data.num1 * data.num2;
            break;
        case 'divide':
            result = data.num2 !== 0 ? data.num1 / data.num2 : "Error: Division by zero.";
            break;
        default:
            result = "Invalid operation.";
    }

    // Display the result
    document.getElementById('result').innerText = `Result: ${result}`;
}
