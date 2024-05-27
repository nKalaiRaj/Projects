#Python program to find Total Holiday Cost
#Define function hotel cost
def hotel_code(no_night,price): #Input parameters number of night stay and cost per day
    hotel_cost = no_night * price #Calculate hotel cost
    return hotel_cost #Return the hotel cost
#Define Function to find plane cost based on city
def plane_cost(city):
    
    if city == 'London':     #Check city and get the plane cost accordingly
        plane_cost = 50
    elif city == 'Paris':
        plane_cost = 100.45
    elif city == 'America':
        plane_cost = 150.99
    elif city == 'France':
        plane_cost = 65
    else:    
        plane_cost = 75
    
    return plane_cost    #Return plane cost
#Define function to get the cost of Car hired
def car_rental(no_days,price):  # Input parameter number of day car hired and cost per day
    car_cost = no_days * price #Calculate cost per day
    return car_cost #return cost of car hired for all days 
#Define function to get total holiday cost
def holiday_cost():
    number_night = int(input("Number of night stay in hotel : "))# User input number of night stay
    hotel_price =  float(input("Hotel Price per night : "))#User input hotel cost per night
    hotelcost  = hotel_code(number_night,hotel_price)# Calling function to get hotel cost
    #print(hotelcost)
    holiday_city = input("Enter city to travel (London,Paris,America,France,others) : ").capitalize() #USer input City
    planecost = plane_cost(holiday_city) #Calling function to get plane cost based on city entered
    #print(planecost)
    car_rental_day = int(input("Number of days Car hired : ")) #User input number of days car hired
    car_price = float(input("Price of Car hired per day : "))#USer input price of hiring car per day
    carcost = car_rental(car_rental_day,car_price)#Calling function to get car cost
    #print(carcost)
    Total_cost = hotelcost + planecost + carcost # Calculating total cost by adding money spent in hotel,plane and car hired 
    print ("Total Holiday Cost is : " + str(Total_cost)) #Display total cost

print("--**-- Vacation Cost --**--")
holiday_cost() #Calling function to get and print the Holiday cost detail.


