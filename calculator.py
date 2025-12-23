def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Div by 0"

def main():
    print("--- Modular Calculator ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    
    choice = input("Select operation (1-4): ")
    x = float(input("First number: "))
    y = float(input("Second number: "))

    operations = {'1': add, '2': subtract, '3': multiply, '4': divide}
    
    if choice in operations:
        result = operations[choice](x, y)
        print(f"Result: {result}")
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()
