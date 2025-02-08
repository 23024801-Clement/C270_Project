from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            # Get the input numbers and operation from the form
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            operation = request.form.get("operation")

            # Perform the calculation
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2 if num2 != 0 else print("Error: Division by zero")
            else:
                result = print("Invalid Operation")
        except Exception as e:
            result = f"Error: {e}"

    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    # Run Flask on port 8080
    app.run(host="0.0.0.0", port=5050)
