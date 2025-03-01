def practice1():
    while True:
        try:
            num1 = float (input("Enter first number: "))
            num2 = float (input ("Enter second number: "))

            if num1 > num2:
                print (num1)
            else:
                print (num2)
        
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
                return None
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
        except ValueError:
            print ("Please enter a numeric number!")
            continue

practice1()
