#Python program to display each word of a sentence in separate line.
sentence = input("Enter a sentence : ") #Request user to input a sentence
print(sentence) # Display the sentence 
sentence_split  = sentence.split() #Split the sentence in form of list 
print(sentence_split) # Display list
sent_join = "\n".join(sentence_split) #Join the list using \n - Newline Escape character.
print(sent_join) #Display the result : each word of a sentence in separate line.