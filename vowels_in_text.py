#Python program to display length of character ,word ,lines and number of vowels present in text file.
vowel_list= ['a','e','i','o','u','A','E','I','O','U']  #Initialize the vowels
count = 0               #Initialize count as zero
with open("input.txt",'r') as file:  #open the file in read mode
    data = file.read()       #Read the file into variable
    character = data.replace(" ","")  #remove the space by replacing the no null space
    print(f"Length of Character : {len(character)}")  #Display length of characters
    line = data.splitlines() #Split the line
    line_len = len(line)    # length of line
    print(f"Length of line : {line_len}")  #Display length of line
    word = data.split()     # split the text as list 
    word_len = len(word)    # get the lenght of word
    print(f"Length of word : {word_len}")  #Display the length of word
    for vowel in data:           #Loop through the text
        if vowel in vowel_list:   # if vowels from list is checked with text from file if it exits 
            count += 1                   #Increase the count by one 
    print(f"No of Vowels is : {count}") #Display the output no of vowels inside the file.