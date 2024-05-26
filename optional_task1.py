#Python program to input a number more than 10 and print the number same times
num = int(input("Enter a number :")) #Request user to input a number
if num > 10:                         #check if the number is greater than 10
    for i in range(0,num):           #Using for loop taking the range from 0 to number entered
        print(num)                   #Display the number within the loop
else:
    print("Sorry,too small")         #Display sorry,too small.

