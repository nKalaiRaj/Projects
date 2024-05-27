#Python program : Simple Calculator that handles Exceptions
#Inside while loop when True
def simple_calculation():
    while True: 
        ''' User Input two numbers as num1 and num2,using try and except 
        method both the numbers are validated and captures error message    
    '''        
        try:
            num1 = float(input("Enter the First number: "))
            num2 = float(input("Enter the Second number: "))            
        except ValueError as error:            
            print("Please enter a valid number")
            print(error)
            continue

        operator = input("Enter Operator [ *,-,+,/ ]: ") #User Input Operator
        #Checking the condition for +,-,/,*
        if operator == '+': #Addition
            sum = num1 + num2
            Equation =  f"Sum Equation : {num1} + {num2} = {sum}\n"
            print(Equation)

        elif operator == '-': #Subtraction
            minus = num1 - num2
            Equation = f"Minus Equation : {num1} - {num2} = {minus}\n"
            print(Equation)  

        elif operator == '*': #Multiplication
            product = num1 * num2
            Equation = f"Product Equation : {num1} * {num2} = {product}\n"
            print(Equation)

        elif operator == '/': #Division
            #Exception is handled to Display Zero Division Error
            try:
                divide = round(num1/num2,2)
                Equation = f"Divide Equation : {num1} / {num2} = {divide}\n"
                print(Equation)
            except ZeroDivisionError as Error:
                print("Cannot divide by Zero.")
                print(Error)
                print("Try Again")
                continue    #Loop does not break and ask user to input numbers again

        else:
            print("Enter valid Operator : ") #Display Message if any invalid Operator is entered.
            break

        break   #Loop breaks to enter number again and valid operator

    #Writing into a file in append mode 
    with open("MathEquation.txt",'a') as file:       
        file.writelines(Equation)

'''Request user enter file name, displays error msg if file not found. Also displays error msg
if incorrect file name is entered.Request user to Enter the correct text file.
    '''
simple_calculation()

while True:     
    try:
        User_input = input("Enter the filename to view the equation text file (MathEquation.txt) or Enter (Calculate) to enter two numbers: ").lower()
        #Checking if MathEquation text file exits
        if User_input == ('MathEquation.txt').lower():    
            try:
                file = open("MathEquation.txt",'r')
                MathEquations = file.read()
                print(MathEquations)           # Display the equation text file
                break
            except FileNotFoundError as Error:
                print("The file that you are trying to open does not exists.")
                print(Error)
                break
        #Checking if Calculate exists to again calculate two numbers with given operator  
        elif User_input == ('Calculate').lower():
            try:
                simple_calculation()
                continue
            except Exception:
                print("Enter the correct name (Calculate )and Try Again!")
        else:
                 print("Enter the correct file name as MathEquation.txt and Try Again!") 
                 continue            #Continue to try again if the user input wrong file name
    except Exception:
            print("Try Again!")


