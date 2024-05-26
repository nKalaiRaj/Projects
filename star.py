import math    # Import math function for calculation of GCD
#Program to count down from 20 to 0 using while loop
print("Count down from 20 to 0 ")
i = 20
while i >= 0:
    print(i)        #Display value from 20 to 0
    i -= 1          #Decreasing the value by 1
# Display all even numbers from 1 to 20 using any loop
print("Display all Even number between 1 and 20")
for i in range (0,21):
    if i%2 == 0:       #checking the number using mod function
        print(i)       #Display all the even number

#Using loop print *
stars = "*"
for i in range (1,6):   # i value ranges from 1 to 5 as last digit takes one less number
    print(stars)        # Display * in increasing order
    stars = stars + "*" # Increments star

# Greatest common divisor of two numbers
num1 = int(input("Enter the first positive number : ")) #Request user input first positive number
num2 = int(input("Enter the second positive number : ")) #Request user input second positive number
GCD = math.gcd(num1,num2)   #Using math.gcd function get the result of gcd
print(GCD)  #Display GCD