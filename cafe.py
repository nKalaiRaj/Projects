#Python program to get total stock worth in cafe.
#Menu list with four items
Menu = ['Donuts','Croissant','Coffee','Bagels']
#Stock dictonary with menu items and its value
stock = {'Donuts': 20,'Croissant': 10,'Coffee': 45,'Bagels': 15}
#Price dictonary with menu items and its price of each item
Price = {'Donuts': 2 , 'Croissant': 3 ,'Coffee': 3.50 ,'Bagels': 1.50 }
stock_price = 0 #Initialize the value of stock price as zero
for i in stock: #For each item in menu 
    stock_price += stock[i] * Price[i] #Calculating the total item value and its price of all items
print(f"Total stock worth in cafe is : £{stock_price}") #Displaying the total stock proce