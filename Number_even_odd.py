# Program for finding Even numbers:
# Request the user to enter the number to identify the even numbers until then
num = int(input("Enter a number : "))
# Initialize the variable to zero
i = 0
# Using condition while loop if the value is less than given number 
while i <= num:
    i += 1 # Increment the value by 1
    if i % 2 == 0: # Using MOD , if the value is equal to Zero
        print(f"All Even numbers from 1 until {num} : {i}") # Display the output
       



