#Python program which takes user input and display all names 
name_list = []    #Initialize the empty string
i = 0             #Initialize variable i set to 0
while i >= 0:     #While i greater than 0
    name = input("Enter the name (John to exit): ").lower() #Request user input names
    if name == "john": #End and print all the names when string John is entered
        break    #Break and exit the loop
    else:
        name_list.append(name)  #add all the names into the list using append()
    i += 1        #Increment value of I by 1
print(name_list)   #Print all the list of names