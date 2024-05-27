#Python program to get the meaning of given abbrevation
# Enter the dictonary abbrevation and its meaning in a variable
dict_abbr = {   'API':'Application Programming Interface',
                'IDE' : 'Integrated Development Environment',
                'SDK' : 'Software Development Kit',
                'OOP' : 'Object Oriented Programming',
                'SSH': 'Secure Shell' }
#adding two more key and their meaning to dictonary
dict_abbr['HTTP'] = 'Hypertext Transfer Protocol'
dict_abbr['HTML'] = 'Hypertext Markup Language'
#Request user Input abbrevation
abbr = input("Enter the Abbrevation : ")
#Checking if the abbreviation exists in dictonary 
if abbr in dict_abbr.keys():
    print(f"{abbr} : {dict_abbr[abbr]}") #If exists display abbreviation and meaning
else:
    print("Abbreviation not found.")   #display abbreviation not found  
