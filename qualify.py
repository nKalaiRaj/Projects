#Entering the time as input for three events like swimming,cycling,running.
swimming = int(input("Enter the time taken to complete the swimming task in minutes : "))
cycling = int(input("Enter the time taken to complete the cycling task in minutes : "))
running = int(input("Enter the time taken to complete the running task in minutes : "))
#Calculate the qualify time by adding time taken for all three events.
qualify_time = swimming+cycling+running
#Display Total time taken for Triathlon
print(f"Total time taken for Triathlon is : {qualify_time}")
#checking the qualifying time and display the award
if qualify_time <= 100: 
    print("Awarded Provincial colours")
#Within five minutes of qualifying time display the award     
elif qualify_time>100 or qualify_time<=105:
    print("Provincial Half Colours")
#Within ten minutes of qualifying time display the award     
elif qualify_time>105 and qualify_time<=110:
    print("Provincial Scroll")
#More than ten minutes of qualifying time display the award     
else:
    print("No Award")    

