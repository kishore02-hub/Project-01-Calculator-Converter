
def get_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid input! Please enter a number.")


while True:

    print("\n===== TIGER CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Kilometers to Miles")
    print("6. Celsius to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        print("Result:", num1 + num2)

    elif choice == "2":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        print("Result:", num1 - num2)

    elif choice == "3":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        print("Result:", num1 * num2)

    elif choice == "4":
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero!")

    elif choice == "5":
        km = get_number("Enter kilometers: ")
        miles = km * 0.621371
        print("Miles:", miles)

    elif choice == "6":
        celsius = get_number("Enter temperature in Celsius: ")
        fahrenheit = (celsius * 9/5) + 32
        print("Fahrenheit:", fahrenheit)

    elif choice == "7":
        print("Thank you for using TIGER CALCULATOR!")
        break

    else:
        print("Invalid choice! Please select 1-7.")
