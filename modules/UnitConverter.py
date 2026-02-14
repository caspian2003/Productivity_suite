class UnitConverter:
    def run(self):
        print("1. cm to m\n2. kg to g\n3. C to F")
        ch = input("Choice: ")
        try:
            val = float(input("Enter value: "))
            if ch == "1":
                print(val / 100, "m")
            elif ch == "2":
                print(val * 1000, "g")
            elif ch == "3":
                print((val * 9/5) + 32, "F")
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input")