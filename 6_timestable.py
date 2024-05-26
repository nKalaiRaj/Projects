#Python program to display the times table
number = int(input("Enter the number :")) # Request user to enter any number
#using for loop choosing the range from 0 to the entered number.(our case is only for 6 times table)
for x in range (number,number+1): 
    for y in range (1,13): #using for loop choosing the range from 0 to 12
        print(f"{x} * {y} = {x*y}") #Display in times table format 