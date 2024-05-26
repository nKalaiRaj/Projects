# Program to find Total number of Pupils entered:
i = 0                     # Initialize the value of i as 0
while i >= 0:             # while the value of i is greater than or equal to 0
    #Request the user to enter the pupils names
    name = input("Enter the name of the Pupils in Class (Enter Stop to Exit.) : ")
    if name.lower() == 'stop':  # Stop entering the puplis name
        print(f"Total number of name's user entered :{i}") #Display Total number of pupils entered
        break    # break to come out of loop
    i += 1        # increment the value of i by 1 to continue the loop