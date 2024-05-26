# This example program is meant to demonstrate errors.

# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print ("Welcome to the error program")   # parenthesis were missing in print statement : Syntax error
print ("\n")                           # Indentation error and syntax error missing parenthesis:
# IndentationError: ageStr variable is assigned withouting defining , only one equal sign should be used 
ageStr = 24  #I'm 24 years old.   # IndentationError: ageStr variable is assigned without2 defining
age = ageStr                        # IndentationError: unable to convert string to int
print("I'm" + str(age) + "years old.")   # IndentationError: and TypeError: can only concatenate str (not "int") to str
three = 3     # IndentationError:

answerYears = age + three   # IndentationError: type error ... three is not a int variable.. change to integer input
#SyntaxError: Missing parentheses  : "answerYears" logical error.. should not be with quotations marks in print statement
print ("The total number of years:" + str(answerYears) ) #TypeError: can only concatenate str (not "int") to str
#NameError: name 'answer' is not defined ..NameError: name 'answer' is not define and 6months is missed
answerMonths = (answerYears * 12) + 6  # Add 6 to get 6months more
#SyntaxError: Missing parentheses and TypeError: can only concatenate str (not "int") to str
print ("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old") 

#HINT, 330 months is the correct answer

