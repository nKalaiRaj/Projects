#Python program that strips a set of characters from a string
string = input("Enter the string : ") #Request user input a string
print(string) #Display string
vowels = 'a,e,i,o,u'  # Assign characters to be striped
split_vowels = vowels.split(',') #Split the vowels in form of list
print(split_vowels) #Display the list
string_replace = '' #Initialize variable to an empty string
for i in range(len(string)): # Loop each string character  
    if string[i] not in split_vowels: #Check if string character not in vowel list
        string_replace += string[i] #append all the character to string_replace variable
print(string_replace) # Display output
        
