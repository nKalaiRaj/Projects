#Python program that acts as calculator
#Define function to add two numbers
def add_num(num1,num2):
    add = num1 + num2
    return add
    
#Define function to subtract two numbers
def subtract_num(num1,num2):
    subtract = num1 - num2
    return subtract

#Define function to multiply two numbers
def multiply_num(num1,num2):
    multiply = num1*num2
    return multiply

#Define function to divide two numbers
def divide_num(num1,num2):
    divide = num1/num2
    return divide

#Define function to print menu
def print_menu():
    print(" Option 1 - add")
    print(" Option 2 - subtract")
    print(" Option 3 - multiply")
    print(" Option 4 - divide")
    print()

#Request user to enter two numbers
number1 = int(input("Enter the first Number: "))
number2 = int(input("Enter the second Number: "))
print_menu()    #Display Menu
menu_option = int(input("Enter the Menu Options :")) #Request user enter menu option
while True: #While true
    if menu_option == 1:       #Check if option 1 
        sum = add_num(number1,number2) #Calling function add
        print(f"Addition of {number1},{number2} is : {sum}")
        break
    elif menu_option == 2:#Check if option 2 
        subtract = subtract_num(number1,number2) #Calling function subtract
        print(f"Subtraction of {number1},{number2} is : {subtract}")
        break
    elif menu_option == 3:#Check if option 3 
        multiply = multiply_num(number1,number2) #Calling function multiply
        print(f"Multiplication of {number1},{number2} is : {multiply}")
        break 
    elif menu_option == 4:#Check if option 4 
        divide = divide_num(number1,number2)#Calling function divide
        print(f"Division of {number1},{number2} is : {divide}")
        break  