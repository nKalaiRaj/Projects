i = 0 # Initialize the value of i as 0
sum = 0 # Initialize the value of sum as 0
while i >=0: # while the value of i greater than or equal to 0
    num = int(input("Enter a number (-1 to Exit ) : ")) #Request user to enter a number
    i += 1 # increment the value of i by 1 to continue the loop
    if num == -1: #while number is equal to -1
        print(f"Sum of the given numbers {sum}")  #Display the sum
        print(f"Average of given numbers : {avg}") #Display the Average
        break
    else:    
        sum += num # Add the given entered number and assign as sum
        avg = sum/i # calculate average by divinding the sum by total number of input numbers
        
        



