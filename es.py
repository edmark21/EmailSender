import getpass, os, sys
import smtplib
from email.mime.text import MIMEText

e = '1'

banner1 ='''


███████╗███╗   ███╗ █████╗ ██╗██╗         ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗██║██║         ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║██║         ███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                            
                Email Loaded [''' + e + ''']


            [1] Start
            [2] Option
            [3] About
            
'''

op2 = '''

 +++++++++++++++++++++++
 +   Account Setings   +
 +++++++++++++++++++++++

    [1] Add Account
    [2] See Account
    [3] Remove Account


 '''

abt = '''

        About

        App version 1
        Build and Created by:
        Edmark Jay Sumampen

        This tool is created to automate email
        send email in a short period of time.

        how to setup?
        

        App Password url: https://myaccount.google.com/apppasswords
        

'''


def load_credentials(filename="credentials.txt"):
    """Loads the username and password from a file.

    Args:
        filename (str, optional): The name of the file to load the credentials from. Defaults to "credentials.txt".

    Returns:
        tuple: A tuple containing the username and password, or None if the file cannot be read or the credentials are not in the expected format.
    """

    try:
        with open(filename, "r") as file:
            line = file.readline()
            username, password = line.strip().split(":")
            return username, password
    except (FileNotFoundError, IOError):
        print("Error: Could not find or read credentials file.")
        return None


def send_email():

    credentials = load_credentials()
    if credentials:
        username, password = credentials
        #print("Username:", username)
        #print("Password:", password)


        """Sends an email with a subject and message.

        Raises:
            smtplib.SMTPException: If an error occurs during email sending.
        """

        sender = username
        receiver = "abarskie112000@gmail.com"
        password = password  # Replace with your actual password (store securely)

        # Create a message object with subject and body
        message = MIMEText("test ni siya", _charset="utf-8")
        message["Subject"] = "Iyot"  # Replace with your desired subject

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, receiver, message.as_string())
                print("Message sent successfully! ==> " ,receiver)
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")

    else:
        print("No credentials found.")
        input("\nReturning to Main Menu....")
        main()


    






def get_credentials():
    """Prompts the user for a username and password, and returns them as a tuple."""

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

def save_credentials(username, password, filename="credentials.txt"):
    """Saves the username and password to a file.

    Args:
        username (str): The user's username.
        password (str): The user's password.
        filename (str, optional): The name of the file to save the credentials to. Defaults to "credentials.txt".
    """

    with open(filename, "w") as file:
        file.write(f"{username}:{password}\n")
    print("Credentials saved successfully!")








    





def main():
    os.system("cls")
    print(banner1)
    

    opt_butang = input("Select Option [1-3]: ")

    if opt_butang == "1":
        print("Starting......")
        send_email()

        
    elif opt_butang == "2":
        print(op2)
        opt = input("Select Option [1-3]: ")
        if opt == "1":
            username, password = get_credentials()
            save_credentials(username, password)
            input("\n\nPress Enter to Continue....")
            main()
            
        elif opt == "2":
            credentials = load_credentials()
            if credentials:
                username, password = credentials
                print("Username:", username)
                print("Password:", password)
            else:
                print("No credentials found.")

            input("\n\nPress Enter to Continue....")
            main()
            


            
        elif opt == "3":
            print("comming soon")
            input("\n\nPress Enter to Continue....")
            main()
            
            
        else:
            input("error pls select only [1-3]: ")
            main()

    elif opt_butang == "3":
        print(abt)
        input("\n\nPress Enter to Continue....")
        main()
        

    else:
        print("error pls select only [1-3]")
        main()




        
    
main()
