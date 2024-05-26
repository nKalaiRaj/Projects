pac_price = int(input("Enter the price of package : "))     # Request user price of package 
distance = int(input("Enter the total distance of the delivery in Kms :")) # Request user total distance in Kms
delivery_pref_air = input("Enter the delivery preference 'A for Air and F for Freight' : ") # Request user delivery preference A or F
delivery_pref_insur = input("Enter the delivery preference 'F for Full insurance or L for limited insurance' : ") # Request user delivery preference F or L
delivery_pref_gift = input("Enter the delivery preference 'G for Gift or NG for no gift' : ") # Request user delivery preference G or NG
delivery_pref_prio = input("Enter the delivery preference 'P for Priority or SD for Standard Delivery' : ") # Request user delivery preference P or SD
if delivery_pref_air == "A":                        # Check if delivery preference is Air 
    delivery_cost = pac_price + (distance * 0.36)   # Calculate delivery cost by adding the package price and multiplying the distance with cost per Km by air
    print(" Total delivery cost by Air: {}".format(delivery_cost)) # Display delivery cost by Air
else :     #delivery_pref == "freight"              # else
    delivery_cost = pac_price + (distance * 0.25)      # Calculate delivery cost by adding the package price and multiplying the distance with cost per Km by freight
    print(" Total delivery cost by freight: {}".format(delivery_cost)) # Display delivery cost by frieght
if  delivery_pref_insur == "F":                         # Check if delivery preference is F for Full Insurance 
    delivery_cost = delivery_cost + 50.00               #Calculate delivery cost by adding the delivery_cost and R50.00
    print(" Total delivery cost with full insurance: {}".format(delivery_cost)) # Display delivery cost for Full Insurance    
else :                                                         # else
    delivery_cost = delivery_cost + 25.00                       # Calculate delivery cost by adding the delivery_cost and R25.00
    print(" Total delivery cost with limited insurance: {}".format(delivery_cost)) # Display delivery cost for limited Insurance 
if  delivery_pref_gift == "G":                                      # Check if delivery preference is Gift
    delivery_cost = delivery_cost + 15.00                           # Calculate delivery cost by adding the delivery_cost and R15.00
    print(" Total delivery cost with Gift: {}".format(delivery_cost))                # Display delivery cost with Gift 
else:                                                                           #else
    delivery_cost = delivery_cost + 00.00                                       # Calculate delivery cost by adding the delivery_cost and R00.00 
    print(" Total delivery cost with no gift: {}".format(delivery_cost))        # Display delivery cost with no gift 
if  delivery_pref_prio == "P" :                                                 # Check if delivery preference is Priority
    delivery_cost = delivery_cost + 100.00                                      # Calculate delivery cost by adding the delivery_cost and R100.00 
    print(" Total delivery cost with Priority: {}".format(delivery_cost))       # Display Total delivery cost with priority
else :                                                                          # else
    delivery_cost = delivery_cost + 20.00                                       # Calculate delivery cost by adding the delivery_cost and R20.00
    print(" Total delivery cost with standard: {}".format(delivery_cost))       # Display Total delivery cost with Standard





