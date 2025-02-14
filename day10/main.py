from art import logo

print(logo)
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self): return self.num1 + self.num2
    def subtract(self): return self.num1 - self.num2
    def multiply(self): return self.num1 * self.num2
    def divide(self): return self.num1 / self.num2 if self.num2 != 0 else "Error! Division by zero."

def main():
    operations = {'+': 'add', '-': 'subtract', '*': 'multiply', '/': 'divide'}
    
    operator = input("Choose an operation (+, -, *, /): ").strip()
    if operator not in operations:
        print("Invalid operator.")
        return

    try:
        num1, num2 = int(input("First number: ")), int(input("Second number: "))
        calculator = Calculator(num1, num2)
        result = getattr(calculator, operations[operator])()
        print(f"Result: {result}")
    except ValueError:
        print("Invalid value!")

if __name__ == "__main__":
    main()
