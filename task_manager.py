# Python program Capstone Project 2 
#Importing libraries
import os
from datetime import datetime ,date

DATETIME_STRING_FORMAT = "%Y-%m-%d" # Assigning date format
# check Task list if exist in python folder
if not os.path.exists("tasks.txt"):
    with open("tasks.txt",'w') as default_file:
        pass
with open("tasks.txt",'r') as task_file:            #Open and read the task detail
    task_detail = task_file.read().split('\n')
    
    task_detail = [t for t in task_detail if t != ""]
    

#  Login Section
# Check if user.txt not exists and create a default txt file
if not os.path.exists("user.txt"):
    with open("user.txt",'w')as default_file:
        default_file.write("admin;pwd")
        pass
#read the username and password details from the text file
with open("user.txt",'r') as user_file:
    user_detail = user_file.read().split('\n') 

#Converting as directory
user_pwd = {}
for user in user_detail:  #Using loop adding the user detail to a dictonary
    
    cusername , password = user.split(";")
    user_pwd[cusername] = password
    
# Menu Function 
def print_menu():  

    if cusername == 'admin':     #for Admins
        task = input(''' Select one of the function below:
            r  - Registering a user
            a  - Adding a task    
            va - viewing all task
            vm - viewing my task
            gr - generate reports
            ds - Display statistics
            e -  Exit        \n :  ''').lower()
    else:                                   #For everyone
        task = input(''' Select one of the function below:
        r  - Registering a user
        vm - viewing my task
        e -  Exit        \n :  ''').lower()
    
    return task   

#Adding new task
task_list = []  
for t_str in task_detail:
    
    curr_t={}
    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['Username'] = task_components[0]
    curr_t['Task_Title'] = task_components[1]
    curr_t['Task_Decription'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)
    
#Function for Registering user
def reg_user():    
#Request input of new user name
    n_user_name = input("Enter New Username :")
            #Request input of new password
    n_password  = input("Enter New Password : ")
            #Request input new password confirmation
    c_password = input("Confirm Password : ")
            #Check if new password entered and password confirmation are same
    if  n_user_name in user_pwd.keys():

        print("Username already exists.Please enter a new username "'\n')

    elif n_password == c_password :
        print("New User added.")
        user_pwd[n_user_name] = n_password
                # Write the new user and pwd into text file.
        with open("user.txt",'w') as out_data: #open file in write mode
            user_detail =[] 
            for n_user in user_pwd:
                user_detail.append(f"{n_user};{user_pwd[n_user]}")#append the list with new username and password
            out_data.write('\n'.join(user_detail))
            print(user_detail)
            # Display error msg    
    else:
        print("Password do not match! ")    
#Function for adding task
def add_task():

    task_username = input("Name of a person assigned to a task : ") #Request user admin to assign a task

    if task_username not in user_pwd.keys(): #A username of the person whom the task is assigned to
        print("User does not exists.Please enter a valid username")
        task = print_menu() 
        if task == 'a':
            add_task()
        else:
           print("User does not exists.Please enter a valid username")
           
    task_title = input("Title of task : ")  #A title of a task,
    task_description = input("Description of Task : ")  #A description of the task
    ''' Add the data to the file tasks.txt and
            Include 'No' to indicate if the task is complete.'''
    current_dt = date.today() #Get todays date
    while True:     #checking if due date entered is correct format
        try:
            task_due_date = input("Due date of task format 'YYYY-MM-DD' : ")
            due_date_time = datetime.strptime(task_due_date,DATETIME_STRING_FORMAT)
            print(due_date_time )
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    new_task = {                  # assigning the new task in a variable 
        "Username":task_username,
        "Task_Title":task_title,
        "Task_Decription":task_description,
        "due_date" : due_date_time,
        "assigned_date": current_dt,
        "completed": False
                }
             #Appending the new task in task list
    task_list.append(new_task)
    print(task_list)   
    with open("tasks.txt",'w') as out_taskfile:   #open file and write in task file
        task_list_to_write = []    
        for t_str in task_list:
            str_attrs = [
                t_str['Username'],
                t_str['Task_Title'],
                t_str['Task_Decription'] ,
                t_str['due_date'].strftime(DATETIME_STRING_FORMAT),
                t_str['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t_str['completed'] else "No"  
            ]
            task_list_to_write.append(';'.join(str_attrs)) #Write into a file
        out_taskfile.write("\n".join(task_list_to_write))
    print("Task successfully added.")
#Function to view all task
def view_all():
    '''Reads the task from tasks.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''
    for tsk_l in task_list:
            disp_str  = f"Task : \t\t {tsk_l['Task_Title']}\n"
            disp_str += f"Assigned To: \t {tsk_l['Username']}\n"
            disp_str += f"Date Assigned: \t {tsk_l['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Due Date: \t {tsk_l['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {tsk_l['Task_Decription']}\n"
            print(disp_str)
#Function to view all my task
def view_mine():
    '''Reads the task from tasks.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
    for idx , tsk_l in enumerate(task_list,1):        
        if tsk_l['Username'] == cusername or cusername == 'admin':              
            disp_str = f"Task: {idx}  \t {tsk_l['Task_Title']}\n"
            disp_str += f"Assigned to: \t {tsk_l['Username']}\n"
            disp_str += f"Date Assigned: \t {tsk_l['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {tsk_l['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {tsk_l['Task_Decription']}\n"
            disp_str += f"Completed: \t {tsk_l['completed']}\n"
            print(disp_str)
    
    if tsk_l['Username'] == cusername or cusername == 'admin': #Check if task exist for tat user and admin too
        task_no = int(input("Enter the task to complete or (-1 to Exit) : "))
        i= 0
        while i < len(task_list): #Iterating though all tasks
            if task_no == idx:
                mark = input("Choose either (Mark the task as complete) or (edit the task) : ")
                if mark == 'Mark the task as complete'.lower():
                    task_list[idx-1]['completed'] = 'Yes'   #updating task completed as Yes
                                        
                elif mark == 'edit the task'.lower() and task_list[idx-1]['completed'] != 'Yes':
                    assigned_date =   input("Change Date Assigned to  'YYYY-MM-DD' : ")
                    #Updating assigned date and due date
                    task_list[idx-1]['assigned_date'] = datetime.strptime(assigned_date,DATETIME_STRING_FORMAT) 
                    due_date = input("Change Due Date to  'YYYY-MM-DD' : ")
                    task_list[idx-1]['due_date'] = datetime.strptime(due_date,DATETIME_STRING_FORMAT) 
                else:
                    print("Please enter either (Mark the task as complete) or (edit the task) : ")                                
                    break
                with open("tasks.txt",'w') as out_taskfile:  #write data into tasks.txt file
                    task_list_to_write = []    
                    for t_str in task_list:
                        str_attrs = [
                            t_str['Username'],
                            t_str['Task_Title'],
                            t_str['Task_Decription'] ,
                            t_str['due_date'].strftime(DATETIME_STRING_FORMAT),
                            t_str['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                            "Yes" if t_str['completed'] else "No"  
                            ]
                        task_list_to_write.append(';'.join(str_attrs))
                        out_taskfile.write("\n".join(task_list_to_write))

                print("Task successfully updated.")
            #Condition to enter correct task number      
            elif task_no != idx and idx != -1 and tsk_l['Username'] != cusername:
                print(f"Please enter the correct task number from 0 to {len(task_list)}")
                break
            else:    #Exit out
                task_no == -1
                break    
        i += 1
    else:
        print("No task available for you!")                    
      
#Function to generate report 
def generate_report():
    Today = datetime.today() #Get todays date
    Total_task = len(task_list) 
    Task_completed = 0
    Task_due = 0
    with open("task_overview.txt",'w') as task_ov_file:  #Generate taskoverview file        
        for t in task_list:
            if t['completed'] :    #Count Completed task
                Task_completed += 1
            if t['due_date'] > Today : #Checking if task is overdue by comparing with today date
                Task_due += 1
        Total_completed_task =  Task_completed    #Calculating total completed task
        Total_uncompleted_task = Total_task - Task_completed #Calculating total uncompleted task
        Total_task_due = Task_due #Calculating total due tasks
        percentage_incomplete = round((Total_uncompleted_task/Total_task)*100,2) #Calculating percentage incomplete task
        percentage_overdue = round((Total_task_due/Total_task)*100,2)#Calculating percentage overdue task
        #Write taskoverview data into text file
        task_ov_file.write(f''' \t\t\t Task Statistics as on {(Today)}\n     
        The total number of task that has been generated and tracked : {(Total_task)}
        The total number of completed task : {(Total_completed_task)}
        The total number of uncompleted task : {(Total_uncompleted_task)}
        The total number of task that havn't been completed and are overdue: {(Total_task_due)}
        The percentage of task that are incomplete : {(percentage_incomplete)}
        The percentage of task that are overdue: {(percentage_overdue)}
        ''')
    #Write the useroverview data into text file    
    with open("user_overview.txt",'w') as user_ov_file:  #Generate useroverview file 
        Total_users = len(user_pwd)
        user_task ,user_completed_task = 0 ,0 #Initializing user task,user completed task and overdue task as Zero
        incomplete_overdue_task = 0
        for user in user_pwd.keys(): #Iterating user present in user lists
            for t in task_list:
                if t['Username'] == user: #Counting users task
                    user_task += 1
                if t['Username'] == user and t['completed'] == True: #Counting user task and checking completed as True
                    user_completed_task +=1
                if t['completed'] == False and t['due_date'] > Today: #Checking the incomplete overdue task
                    incomplete_overdue_task += 1   
        # Calculating user task details            
        percentage_task_assigned = round((user_task/Total_task)*100,2)#Calulate percentage task assigned
        percentage_task_complete = round((user_completed_task/user_task)*100,2)#Calculate percentage task complete
        user_incomplete_task = user_task - user_completed_task#Calculate user incomplete task
        percent_incomp_task = round((user_incomplete_task/user_task)*100,2)#Calculate perentage incomplete task
        per_incom_overdue_task = round((incomplete_overdue_task/user_task)*100,2)#Calculate percentage incomplete overdue task
        #Write User statistic detail in text file
        user_ov_file.write(f''' \t\t\t User Statistics as on {(Today)}\n
        The overall users registered with task_manager.py : {(Total_users)}
        The overall task that has been generated and tracked : {(Total_task)}
        The total number of task assiged to that user : {(user_task)} 
        The percentage of the total number of task assiged to that user : {(percentage_task_assigned)}
        The percentage of the total number of task assiged and complete : {(percentage_task_complete)} 
        The percentage task that are incompleted : {(percent_incomp_task)} 
        The percentage of task that are incomplete and overdue : {(per_incom_overdue_task)}
            ''')
    print("Report Generated."'\n')        
#Function to generate statistics
def generate_statistics():
    # Checking if the text files are present 
    if not (os.path.exists("task_overview.txt") or os.path.exists("user_overview.txt")):
        print("Generate the text files,files doesn't exists.") 
        generate_report()
    else:
        #Display task statistic
        with open("task_overview.txt",'r') as to_file:
            task_overview_file = to_file.read()                        
            print(task_overview_file)
        #Display user statistic   
        with open("user_overview.txt",'r') as uo_file:
            user_overview_file = uo_file.read()
            print(user_overview_file) 


logged_in = False   # Initialising the login flag as False if user not logged in
while not logged_in:
    print("LOGIN :")
    cusername = input("UserName: ") #Request user name as input
    password = input("Password : ") #Request user password as input
    if cusername not in user_pwd.keys(): #Check if user name exists 
        print("User does not exists.")
        continue
    elif user_pwd[cusername] != password: #Check if user password are same for that user 
        print("Incorrect Password") 
        continue
    else:
        print("Login Successfull.")  #Logged in and flag set as True
        logged_in = True

        
#Main program calling all function 
while True:  
    task = print_menu() #Print Menu
    if task == 'r':     #Registering users
        reg_user()
    elif task == 'a':   #Add task
        add_task()
    elif task == 'va':  #View all task
        view_all()
    elif task == 'vm':  #view my task
        view_mine()
    elif task == 'gr' and cusername == 'admin':  #Generate reports
        generate_report()
    elif task == 'ds':  #Display statistics
        generate_statistics()
    elif task == 'e':   #Exit or quit
        quit()     
