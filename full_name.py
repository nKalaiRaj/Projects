# Pseudo code :  1) Request user's fullname 
# 2) Using IF stmt check if entered name is empty and Display "You haven't entered anything. Please enter your fullname."
# 3) If entered string is less than 4 character then Display "You have entered less than 4 characters.Please make sure that you have entered your name and surname. "
# 4) If entered string is greater than 25 character then Display "You have entered more than 25 characters. Please make sure that you have only entered your fullname."
# 5) Finally Display "Thank you for entering your name."
fullname = input("Enter your fullname : ")
print(fullname)
if fullname == " ":
    print("You haven't entered anything. Please enter your fullname.")
elif len(fullname) <= 4:
    print("You have entered less than 4 characters.Please make sure that you have entered your name and surname. ")
elif len(fullname) >= 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your fullname.")
print("Thank you for entering your name.")    

   

