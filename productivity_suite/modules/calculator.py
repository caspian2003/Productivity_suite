class Calculator:
    def run(self):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
            op = input("Choose operation: ")

            if op == "1":
                print("Result:", a + b)
            elif op == "2":
                print("Result:", a - b)
            elif op == "3":
                print("Result:", a * b)
            elif op == "4":
                print("Result:", a / b if b != 0 else "Cannot divide by zero")
            else:
                print("Invalid operation")
        except ValueError:
            print("Invalid number input")