#Python program to determine whether a given word is a Palindrome.
string = input("Enter the string : ") #Request user input string
print(string) #Display string
reverse_string = ''.join(reversed(string[0:len(string)])) #Slice the string from reverse
print(reverse_string) #Display the reversed string 
if string == reverse_string: # Comparing the string and reversed string are same 
    print("Your word is palindrome.") #Display the word as Palindrome
else:
    print("Your word is not a palindrome.")#Display the word as not Palindrome '''
