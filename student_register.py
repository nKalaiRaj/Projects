#Python program that allows the student to register for an exam venue
i = 1  #initialize the value of i as 1
#Request user number of student registering
Number_of_Student = int(input("How many students are registering : ")) 
#open file in write mode
with open("reg_form.txt","w") as file:
#Using while loop to write and enter all students Id number   
  while i <= Number_of_Student:
    student_id = input("Enter your ID Number : ")  #Get the student Id number
    i += 1  #Increment the value of i
#write details of students into file
    file.write(student_id + "\t" + ' : ...................' + "\n") 
print("ID Number Taken!")