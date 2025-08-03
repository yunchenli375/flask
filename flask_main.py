from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"


@app.route("/greet")
@app.route("/greet/<name>")
def greet(name=""):
    return f"Hello {name}"


def celsius2fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


@app.route("/f/<celsius>")
def f(celsius):
    """Convert Celsius to Fahrenheit."""
    try:
        return f"{celsius} Celsius is {celsius2fahrenheit(float(celsius))} Fahrenheit"
    except ValueError:
        return "Invalid input, please provide a number."


if __name__ == "__main__":
    app.run()