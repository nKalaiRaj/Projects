# Request user input three numbers.
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))
# Using If stmt compareing which is greater num1 or num2
if num1>num2:          #comparing num1 greater than num2
    print (f" {num1} is greater than {num2}. ") 
else:
    print (f"{num2} is greater than {num1}.")
# Determining num1 is odd or even and Displaying the result.
if num1%2 ==0:
    print(f"{num1} is Even number.")
else:
    print(f"{num1} is Odd number.")
# Sorting the three numbers in descending order.
if (num1>num2 and num1>num3):      #If num1 is greater than num2 and num3
    if num2>num3:                   #checking if num2 is greater than num3
        print(f"{num1},{num2},{num3}") #Display num1,num2,num3
    else:                               #else
        print(f"{num1},{num3},{num2}")  #Display num1,num3,num2
if (num2>num1 and num2>num3):       #If num2 is greater than num1 and num3
    if (num1>num3):                 # checking if num2 is greater than num3
        print(f"{num2},{num1},{num3}")#Display num2,num1,num3
    else:                            #else
        print(f"{num2},{num3},{num1}") #Display num2,num3,num1
if (num3>num1 and num3>num2):       #If num3 is greater than num2 and num1
    if(num1>num2):                  #checking if num1 is greater than num2
        print(f"{num3},{num1},{num2}")#Display num3,num1,num2
    else:
        print(f"{num3},{num2},{num1}")#Display num3,num2,num1
        
        
        




              

        
