#Python program to create a function dayof week and print second letter as 'Hello' in sentence.

def day_of_week(): #Define function dayofweek
#Intialise all days of weeks in a list    
    alldayofweek = ['Monday','Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday'] 
    for day in alldayofweek: #Using for loop print all the days of week
        print(day) #Display the days of week
day_of_week() #Calling function to display the days of the week


#Function to get sentence from user and print every second word by Hello

def sentc_replaceword(): #Define function replace every second word in  sentence
    sentence = input("Enter the Sentence : ") #User input sentence
    sent_list = sentence.split() #convert sentence to list using split method
    new_list = [] #Initialise empty string
    for count , sent_list in enumerate(sent_list,0): #Using looping enumerater 
        if count%2 == 0:    # checking for alternate word / second word from list
            new_list.append(sent_list) #Appending the word into new list
            new_list.append("Hello") #appending the second word Hello into new list
    print(' '.join(new_list))    # joining the word and Displaying output 
          

sentc_replaceword()   #Calling the sentence replace function