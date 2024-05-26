year = int(input("Enter the year of Birth : "))          #  Request user to enter year of Birth
current_year = int(input("Enter the current year : "))   #  Request user to enter the current year
older = current_year - year                              #  Calculate the age current minus year of birth
#print(older)
if older >= 18 :                                         # Check if the age is greater or equal to 18, if yes 
    print("Congrats,you are old enough")                 # Display 1above 18 old enough to enter
2014