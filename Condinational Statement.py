
# if-elif statement example
# statement1 -only one if condination
# statement2 - two if and else use korbo
# statement 3- three if else - elif use korbo

try:
    marks = int(input("Enter any number: "))

    if marks >= 80:
        print("A+")
    elif marks >= 70:
        print("A")
    elif marks >= 60:
        print("A-")
    elif marks >= 50:
        print("B")
    elif marks >= 40:
        print("C")
    else:
        print("Fail")

except ValueError:
    print("Please enter a valid number.")


