#Python program to display list with friends name and corresponding ages
friends_name = ["Kalai","Nancy","Sathya"] #Friends names entered in a list
first_friend = friends_name[0]  #Assiging the first friend name
print("First friend name : {}".format(first_friend)) #Display the first friend name
last_friend = friends_name[-1]   #Assign the last friend name entered
print("Last friend name : {}".format(last_friend)) #Display the last friend name
length_of_string = len(list(range(0,len(friends_name)))) #Geting the lenght of string in a list
print("Length of List : {} ".format(length_of_string)) #Display the length
friends_age = []                   #Initializing age list as empty
for name in friends_name:    #Using For loop get the names from name list 
    friends_age = [25,30,33]  #Enter the age of the friends corresponding to their names
print(friends_age) #Display the age
print(friends_name) #Display the name
    