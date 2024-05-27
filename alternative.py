#Python program to convert String character upper and lower alternatively.
string = input("Enter the String :") #Request user input string
string_upper = ""         #Initialize the string as empty string
for i in range(0,len(string)):    #Using For loop find the length of the string
    if i%2 == 0:                   # Using If condition checking if the second character is even and print in upper case else lower case
        string_upper += string[i].upper()
    else:
        string_upper += string[i].lower()
print(string_upper)   #Display the output
str_list = string.split()    #Using Split function split the word in list 
final_str = ""         #Assign a variable to empty string
for j in range (len(str_list)):      #Using for loop getting the len of the string and checking the alternate word
    if j%2 == 0:
        final_str = final_str + ' '+ str_list[j].lower() # Assiging the alternate words to lowercase
    else:
        final_str = final_str + ' ' + str_list[j].upper() # Assiging the alternate words to uppercase
print(final_str.strip())     #Display the output by removing the extra space in front.