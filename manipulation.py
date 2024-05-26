str_manip = input("Enter the String : ")  #Declaring a variable and requesting user input value. 
#print(str_manip)
print(f"length of string is: {len(str_manip)}")        #Displaying the length of string
last_letter = str_manip[-1]                                                   #Get the last letter in the words
print ("Last letter in sentences is : " + last_letter)  #Display the last letter from the sentences
replace_sent = str_manip.replace(last_letter,"@")   # Replace the last letter by @
print ("Replaced Sentences is :" + replace_sent)    #Display the replaced value
print ("Last 3 letters from the sentence is : " + str_manip[len(str_manip):-4:-1]) # prints the last three letters from the sentence
first_three_letter = str_manip[0:3]                 # Assigning the first three letter to a variable
last_two_letter = str_manip[len(str_manip)-2 : len(str_manip) : 1]   # Assigning the last two letter from the sentences 
print (f"First three letter from front and last 2 letter from sentences : {first_three_letter}{last_two_letter}") # Displaying both the output
print ("This \n is \n a \n bunch \n of \n words") # Displaying the words in new line
