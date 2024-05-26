sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!." #Declaring the variable and assigning the values.
replace_sent = sentence.replace("!"," ")      # Replacing "!" with " "space
print(replace_sent)                      # Display the replaced sentence.
upper_sent = replace_sent.upper()       # Changing the sentence to uppercase.
print(upper_sent)                       # Displaying the uppercase sentence.
print (upper_sent[ : : -1] )             # Displaying the uppercase sentence in reverse.