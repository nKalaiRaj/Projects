#Request user input an integer value.
number = int(input("Enter the number : "))
#check if number mod 2 is equal to zero and number mod 5 is equal to zero.
if number%2==0 and number%5==0:
    print("Divisible by 2 and 5") #Display Divisible by 2 and 5
#check if number mod 2 is equal to zero or number mod 5 is equal to zero.    
elif number%2==0 or number%5==0:
    print("Divisible by 2 or 5") #Display Divisible by 2 or 5
else:
    print("Not Divisible by 2 or 5") #Display Not Divisible by 2 or 5