def practice1():
    while True:
        try:
            num1 = float (input("Enter first number: "))
            num2 = float (input ("Enter second number: "))

            if num1 > num2:
                print (num1)
            else:
                print (num2)

            if not again():
                break

        except ValueError:
            print ("Please enter a numeric number!")
            continue

def practice2():
    while True:
        try: 
            num1 = float (input("Enter first number: "))
            num2 = float (input ("Enter second number: "))

            if num1 == num2:
                print ("Equal")
            else:
                print("Not equal")
            
            if not again():
                break

        except ValueError:
            print ("Please enter a numeric number!")
            continue

def practice3():
    while True:
        try:

            num1 = float (input("Enter first number: "))
            num2 = float (input ("Enter second number: "))

            sum = num1 + num2

            print("Sum:", sum)    

            if not again():
                break

        except ValueError:
            print ("Please enter a numeric number!")
            continue

def practice4():
    while True:
        try:

            num1 = float (input("Enter first number: "))
            num2 = float (input ("Enter second number: "))

            product = num1*num2
            print (f"The product is: {product}")

            if not again():
                break

        except ValueError:
            print ("Please enter a numeric number!")
            continue

def practice5():
    while True:
        try:
            num1 = float (input("Enter first number: "))
            num2 = float (input ("Enter second number: "))

            quotient = num1/num2
            print (f"The quotient is: {quotient:.2f}")
            
            if not again():
                break
                
        except ValueError:
            print ("Please enter a numeric number!")
            continue

def practice6():
    while True:
        try:
            num1 = float (input("Enter first number: "))
            num2 = float (input ("Enter second number: "))

            power = num1**num2
            print (f"The result is: {power:.0f}")

            if not again():
                break

        except ValueError:
            print ("Please enter a numeric number!")
            continue

def practice7():
    enter = 10
    sum = 0
    for i in range (enter):
        numbers = float(input(f"Please input number {i + 1}, {9-i} inputs remaining: "))
        
        sum += numbers 

    print (f"Total sum is: {sum}")
    if not again():
        return

def practice8():
    enter = 10 
    odd = []

    for i in range(enter):
        numbers = float(input(f"Please input number {i + 1}, {9-i} inputs remaining: "))
        if numbers %2 != 0:
            odd.append(numbers)
            
        else:
            continue
    
    print ("There are", len(odd), "Odd numbers.")
    if not again():
        return

def practice9():
    for i in range(0,102,2):
        print (i)
    if not again():
        return

def practice10():
    for i in range(0,102,2):
        if i % 10 != 0:
            print(i)
    if not again():
        return

def options():
    while True:
        try:
            pick = int(input("Pick from 1-10 Practice Programs: "))
            if pick == 1:
                practice1()
            elif pick == 2:
                practice2()
            elif pick == 3:
                practice3()
            elif pick == 4:
                practice4()
            elif pick == 5:
                practice5()
            elif pick == 6:
                practice6()
            elif pick == 7:
                practice7()
            elif pick == 8:
                practice8()
            elif pick == 9:
                practice9()
            elif pick == 10:
                practice10()
            else:
                print("Please pick from 1-10 only!")
                continue
        except ValueError:
            print("Invalid input!")
            continue

def again():
    while True:
        a = input("\nDo you want to (R)etry / (E)xit?: ").strip().upper()
        if a == 'R':
            options()
        elif a == 'E':
            exit()
        else:
            print("Invalid input. Please choose between 'R'/'E'.")

options()
