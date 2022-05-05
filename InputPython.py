#defining a variable
try:
    #input is always in string
    age = int(input("Enter your age: "))
    if (age > 150):
        print("Invalid age")
    elif (age < 1):
        print("Invalid age")
    else:
        print("Your age is", age)
except(ValueError):
    print("Invalid input Please enter numbers")


