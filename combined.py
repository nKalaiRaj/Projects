#Python program to sort numbers from two different file and write in another file in ascending order.
allnum_list = []
#Open first file in read mode
with open("number1.txt",'r') as file1:
    Textfile1 = file1.read()     #Read first file and store it in variable
#Open second file in read mode    
with open("number2.txt",'r') as file2:
    Textfile2 = file2.read()     #Read second file and store it in variable
#Numbers to be appended in single file 
Textfile1 += '\n'  #Second file has to be appended from next line
Textfile1 += Textfile2     #Numbers from both file are store in one variable
#Numbers are converted to list for sorting using split method
allnum_list = Textfile1.split()
#Using for loop to convert string to integer and then sort
for i in range(0,len(allnum_list),1):
    allnum_list[i] = int(allnum_list[i]) #Convert from string to integer
allnum_list.sort() #Sort all the numbers in ascending order
#open another file and write all sorted numbers in ascending order
with open("all_numbers.txt",'w') as file3:
    file3.write('\n'.join(str(allnum) for allnum in allnum_list))
print("Numbers written in ascending order !")    