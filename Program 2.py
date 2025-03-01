while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num1 == num2:
            print("Equal")
        else:
            print("Not equal")
    
    except ValueError:
        print("Please enter a numeric number!")
        continue
    
    # Ask if the user wants to try again after successful input
    try_again = input("\nDo you want to try again? (yes/no): ").strip().lower()
    if try_again != 'yes' or try_again != 'y':
        print("Thank you for using the program!")
        break