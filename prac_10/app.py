from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    if name:
        return f"Hello {name}"
    return "Hello"

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

@app.route('/convert/<celsius>')
def convert(celsius):
    try:
        c = float(celsius)
        f = celsius_to_fahrenheit(c)
        return f"{c}° Celsius is {f:.2f}° Fahrenheit"
    except ValueError:
        return "Invalid temperature value."

if __name__ == '__main__':
    app.run(debug=True)