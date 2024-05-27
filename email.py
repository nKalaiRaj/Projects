#An Email Simulation
inbox = []
sentmail = []   
class Email():

    def __init__(self,from_address,email_contents,has_been_read,is_spam):
        self.from_address = from_address
        self.email_content = email_contents        
        self.has_been_read = False
        self.is_spam = False
#create a function for marking the email as read
    def mark_as_read(self):
        if self.has_been_read == False:
            self.has_been_read = True        
#create a function for marking the email as spam
    def mark_as_spam(self):
        if self.is_spam == False:
            self.is_spam = True       
#Add mail to Store
def add_email():
    from_address = input('Enter the email address :')
    email_content = input('Enter your message :')
    new_email =  Email(from_address,email_content,False,False)
    inbox.append(new_email)                 
    print("Email is Added")        
#send messages function
def send_email():
    from_address = input("Enter email address :")
    email_content =  input("Enter email content :")       
    email_send = Email(from_address,email_content,False,False)
    sentmail.append(email_send)
    print("Your Message has been Sent.")
#Get the total msg present in store
def get_count():
    return {f'Number of Message in Inbox :{len(inbox)}'}
#Get the message content
def get_email(idx):      
    view_email = inbox[idx] 
    view_email.mark_as_read()   
    print(f"Email Content is : {view_email.email_content}")
#Display all unread mails
def get_unread_email():
    for email in inbox:
        if email.has_been_read == False :            
            print("From    : ", email.from_address)
            print("Message : ", email.email_content)            
        else:
            print("All mails are read")

#Display all spam mails
def get_spam_email():
    for email in inbox:
        if email.is_spam == True:            
            print("From    : ", email.from_address)
            print("Message : ", email.email_content)            
        else:
            print("No Spam Mails")    

#Delete Mails      
def delete_email(id):
    for email in inbox:
        if inbox.index(email) == id:
            inbox.remove(email)
    print("Email deleted! ")
  
                  
#Creating object of email:

# Adding emails to inbox
email1 = Email("kalai@xyz.com","Welcome to HyperionDev.",False,False)
email2 = Email("selvi@abc.com","Hope your Bootcamp is going well.",False,False)
email3 = Email("jonny@xyz.com","All the very best.",False,False)
unread = []
spam = []
user_choice = ""

inbox.extend([email1,email2,email3])  ## adding all your emails at once to  inbox

## Printing inbox so that user can see the inbox and know which index to choose

for i in inbox:
    print(i.email_content,i.from_address)

while user_choice != "quit":
    
    user_choice = input("What would you like to do - add_email/read/unread/spam/delete/send/quit?")
#Add Email
    if user_choice == "add_email":    
        add_email()            
        continue
#Read Mail    
    if user_choice == "read":
        idx = int(input("Enter the index of email : "))
        get_email(idx)                          
        continue
#Read all unread mails    
    if user_choice == "unread":
        get_unread_email()                                     
        continue 
#read all spam mails    
    if user_choice == "spam":
        get_spam_email()          
        continue
#Delete mails    
    elif user_choice == "delete":
        mail_no = int(input("Enter the mail to delete: "))
        delete_email(mail_no)
        continue 
#Send email           
    elif user_choice == "send":
        send_email()
        continue
    elif user_choice == "quit":
        print("Goodbye")
        break
    else:
        print("Oops - incorrect input")

