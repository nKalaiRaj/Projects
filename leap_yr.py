#Python program to check whether given year and following years are leap year or not
year = int(input("What year do you want to start with ?  ")) #Request the user to enter the year
no_of_year = int(input("How many years do you want to check ? ")) #Request the user to number no of years
# using for loop range from input year to year plus no of years given
for i in range (year,year+no_of_year): 
    if i%4 == 0:    # checking if the number(year) is divisible by 4 or MOD == 0
        print(f"{i} is a leap year.")  #If divisible then Display leap year
    else:
        print(f"{i} isn't a leap year.")   #Else Display not a leap year. 