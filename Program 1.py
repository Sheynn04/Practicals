#This programs processes which number is bigger tapos ididisplay
while True:
    try:
        num1 = float (input("Enter first number: "))
        num2 = float (input ("Enter second number: "))

        if num1 > num2:
            print (num1)
        else:
            print (num2)
        break

    except ValueError:
        print ("Please enter a numeric number!")
        continue