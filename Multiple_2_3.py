i = 101 # Initialize the value of i as -1
while i > 100:    #While i > 100
    num = int(input ("Enter the number less than or equal to 100 : ")) #Request the user to input the number
    i +=1    # Initialize the value of i as i = i +1
    if num <= 100 and i>100:  #Check if num is less than or equal 100 and i >100
        if num%2 == 0:  # Check the number even or odd using MOD
            num1 = num   # assigning num = num1 to store the value of number entered
            num = num1*2 #If num is even multiply it by 2
            print(f"Number {num1} is Even and number multiplied by 2 is: {num}") #Display the output
            break
        else:
            num1 = num  # assigning num = num1 to store the value of number entered
            num = num1*3 #If num is odd multiply it by 3
            print(f"Number {num1} is Odd and number multiplied by 3 is: {num}") #Display the output
            break 
    else:
        print("Try Again and please follow the instructions")   #Request the user to try again and follow the instruction 
