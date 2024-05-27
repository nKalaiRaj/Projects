#Python program to calculate numbers
#Import math module
import math
num_list = []
i = 1
while i <= 10:
    numbers = float(input("Enter numbers integer or float : "))
    num_list.append(numbers)
    i += 1
print(num_list)    
#Display the total/sum of all numbers
Total = sum(num_list)
print("Total of all numbers is : " + str(Total))
#get the value of maximun number in list
max_value = max(num_list)
#Get the index of the max value in list
idx_max_val = num_list.index(max_value)
#Display the index of maximum value
print("Index of Maximum of all numbers is : " + str(idx_max_val))
#get the Minimum value from the list
min_val = min(num_list)
#Get the index of the min value in list
idx_min_val = num_list.index(min_val)
#Display the index of minimum value
print("Index of Minimum of all numbers is : " + str(idx_min_val))
#Get the average of all numbers and round off upto 2digits
average = round(Total/len(num_list),2)
#Display the average output
print("Average of all numbers is : " + str(average))
#Sort the number in the list
num_list = sorted(num_list)
print(f"Sorted List : {num_list}") #Display the sorted number
#Get the median number using the formula Median = {(n+1)/2}
idx_median = int((len(num_list)+1)/2)
#print(idx_median) # Display the index of the median
median_num = num_list[idx_median] #Get the median number from the list
print("Median numbers is : " + str(median_num)) #Display the median number