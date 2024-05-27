#Python program to count the occurance of character and display in dictonary
#Initialize the value of string
string = 'google.com'.lower()
#Initialize dictonary as empty
dict_char = {}
for char in string: #For each character in string
    if char in dict_char: #Checking if the character is present in dictonary
        dict_char[char] += 1  #Increment the character by 1
    else:
        dict_char[char] = 1   #add new character to dictonary
print(dict_char)        #Display the output