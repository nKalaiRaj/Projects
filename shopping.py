import math                                                         # Importing the math module to use mathematical functions
Product1 = input ("Enter the names of the first product : ")        # Request user to enter first product
product2 = input ("Enter the names of the second product : ")       # Request user to enter second product
product3 = input ("Enter the names of the third product : ")        # Request user to enter third product
prd1_price = float(input("Enter the price of first product : "))    # Request user to enter first product price
prd2_price = float(input("Enter the price of second product : "))   # Request user to enter second product price
prd3_price = float(input("Enter the price of the third product : ")) # Request user to enter third product price
Total_of_all = prd1_price + prd2_price + prd3_price                  # Calculating Total of all products
print("Total of all product is : {}".format(Total_of_all))           # Displaying the Total
avg_price = math.ceil(Total_of_all / 3)                              # Calculating the average of all products
print("Average of all Products is : {}".format(avg_price))           # Display the average
print(f"The Total of {Product1},{product2},{product3} is R{Total_of_all} and the average price of the items is R{avg_price}") #Displaying the products and its prices in a sentence
