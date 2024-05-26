# Capstone Project 1 - Variables and Control Structures
# Approached by a small financial company to program financial calculators (Investment and Home Loan repayment calculator)
# Created on 09 Dec 2022 by Kalaiselvi Rajasekar
# IMPORT MATH LIBRARY
import math
# Request user to choose financial calculators (Investment or Bond)
print( '''Choose either 'investment' or 'bond' from menu below to proceed : 
investment  - to calculate the amount of interest you'll earn on your investment
bond        - to calculate the amount you'll have to pay on a home loan ''')
# Get the input and store in a variable finance_calc
finance_calc = input("Choose financial Calculator from the above Menu : ").lower()
#Checking if the user has entered valid input.
if finance_calc != 'investment' and finance_calc != 'bond':
    print ("Enter a valid input!... Choose either 'investment' or 'bond' ")
else:   
# If user selects option as 'investment'    
    if finance_calc == 'investment':
# Request user the amount,interest rate and no of years money is being invested    
        P = float(input("Enter the amount to be deposited :"))
        R = float(input("Enter the interest rate (without %): "))
        T = float(input("Enter no of years : "))
        interest = input("Enter Simple or Compound Interest :").lower()
# If user selects option as 'simple'
        if interest == 'simple':
#Calculate simple interest using the formula A=P*(1+r*t) [r/100 to handle percentage]    
            A =  P*(1+(R/100)*T)
            print(f"Simple Interest : {A}") #Display the simple interest output
# If user selects option as 'compound'    
        elif interest == 'compound':
#Calculate compound interest using the formula A=P(1+r)^t       
            A = P*math.pow((1+(R/100)),T)
            print(f"Compound Interest : {A}") #Display the compound interest output
        else:
            print("Enter valid input 'Simple or Compound ' :")   
# If user selects option as 'bond'              
    elif finance_calc == 'bond':
# Request user the present value of house ,interest rate and no of months to repay the bond   
        P = float(input("Enter the Present Value of the house : "))
        i = float(input("Enter the interest rate : "))
        i = i/(100*12) #[i/100 to handle percentage annually]  
        n = float(input("Enter no of months to repay the bond : "))
#Calculate bond repayment using the formula x=(i*p)/(1-(1+i)^(-n)) 
        x = (i*P)/(1-math.pow((1+i),(-n)))
        print(f"Amount to be repayed each month : {x}") #Display the bond repayment amount