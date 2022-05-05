#make a calculator using python

#four operation +,-,*,/

#input1 --> which operation to do


#input is always taken in string




#making a while loop to keep our program running


userInput="  "

while(userInput!="q"):
    userInput = input("Enter the operator from *,/,-,+  or press q to quit--> ")


    def multiply():

        # input is taken into string format so we need to cast it with int to convert the string values into integers
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        # casting the string into integer
        multiply = int(num1) * int(num2)
        print("Multiplied values for", num1, "and", num2, "is", multiply)


    def addition():

        # input here is taken in string format
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        # casting
        s = int(num1) + int(num2)
        print("Addition of", num1, "and", num2, "is", s)


    def subtraction():

        # input here is taken in string format
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        # casting
        r = int(num1) - int(num2)
        print("subtraction of", num1, "and", num2, "is", r)


    def division():

        # input here is taken in string format
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        # casting
        t = int(num1) / int(num2)
        print("division of", num1, "and", num2, "is", t)


    # logic
    if (userInput == "*" or userInput == "/" or userInput == "+" or userInput == "-"):

        # calculators code
        if (userInput == "*"):
            multiply()

        if (userInput == "+"):
            addition()

        if (userInput == "-"):
            subtraction()

        if (userInput == "/"):
            division()







    else:
        print("Please enter the operation from (+,-,/,*) and try again")



