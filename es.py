import getpass, os, sys, re, json
import smtplib

import gspread, time

from oauth2client.service_account import ServiceAccountCredentials
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def wala():
  try:
    os.system("cls")

  except:
    os.system("clear")
    
wala()




filename = 'credentials.txt'
hmf = input("How many files: ")

a = []

if hmf == "1":
    fina = input(" [1] Enter the filename of the file, ex: file.pdf or file.txt: ")
    a.append(fina)
elif hmf == "2":
    fina = input(" [1] Enter the filename of the file, ex: file.pdf or file.txt: ")
    fina2 = input(" [2] Enter the filename of the file, ex: file.pdf or file.txt: ")
    a.extend([fina, fina2])
elif hmf == "3":
    fina = input(" [1] Enter the filename of the file, ex: file.pdf or file.txt: ")
    fina2 = input(" [2] Enter the filename of the file, ex: file.pdf or file.txt: ")
    fina3 = input(" [3] Enter the filename of the signature file, ex: signature.png: ")
    a.extend([fina, fina2, fina3])
elif hmf == "4":
    fina = input(" [1] Enter the filename of the file, ex: file.pdf or file.txt: ")
    fina2 = input(" [2] Enter the filename of the file, ex: file.pdf or file.txt: ")
    fina3 = input(" [3] Enter the filename of the signature file, ex: signature.png: ")
    fina4 = input(" [4] Enter the filename of the signature file, ex: signature.png: ")
    a.extend([fina, fina2, fina3, fina4])






def count_emails(file_path):
  """Counts the total number of emails in a JSON file.

  Args:
    file_path: The path to the JSON file.

  Returns:
    The total number of emails.
  """

  with open(file_path, 'r') as f:
    data = json.load(f)

  email_count = 0
  for entry in data:
    if 'Email' in entry:
      email_count += 1

  return email_count

# Replace 'extracted_data.json' with the actual path to your JSON file
file_path = 'extracted_data.json'
total_emails = count_emails(file_path) #total email






try:
    with open(filename, 'r') as file:
        for line in file:
            # Check for email format (basic validation)
            if '@' in line and '.' in line.split('@')[-1]:
                email = line.strip().split(':')[0]  # Extract email address only
                break  # Exit the loop after finding the first valid email
except FileNotFoundError:
    print(f"[Please Login first in Option menu]")

try:
    


    banner1 ='''


    ███████╗███╗   ███╗ █████╗ ██╗██╗         ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
    ██╔════╝████╗ ████║██╔══██╗██║██║         ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
    █████╗  ██╔████╔██║███████║██║██║         ███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
    ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
    ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
    ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝


                    Login as: [''' + email + ''']                                                                            
                    Email Loaded [''' + str(total_emails) + ''']


                [1] Start
                [2] Scan
                [3] Option
                [4] About
                
    '''
except:

    banner1 ='''


    ███████╗███╗   ███╗ █████╗ ██╗██╗         ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
    ██╔════╝████╗ ████║██╔══██╗██║██║         ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
    █████╗  ██╔████╔██║███████║██║██║         ███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
    ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
    ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
    ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝


                    Login as: [''' + "No Account Detected" + ''']                                                                            
                    Email Loaded [''' + "0" + ''']


                [1] Start
                [2] Scan
                [3] Option
                [4] About
                
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

        App version 0.4
        Build and Created by:
        Edmark Jay Sumampen

        This tool is created to automate email
        send email in a short period of time.

        how to setup?
        

        visit my app documentation at https://github.com/edmark21/emailsender
        

'''

def removeacc():
    file_path = "credentials.txt"

    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")


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
        print(" Error: Could not find or read credentials file.")
        return None



#####fixing here......


def send_personalized_email(receiver, last_name, template_file="file.txt", attachment_paths=[]):
  """Sends a personalized email with an optional attachment.

  Args:
    receiver (str): The recipient's email address.
    last_name (str): The recipient's last name.
    template_file (str, optional): The name of the template file. Defaults to "file.txt".
    attachment_paths (list[str], optional): A list of paths to attachment files. Defaults to an empty list.
  """

  credentials = load_credentials()
  if not credentials:
    return

  sender, password = credentials

  with open(template_file, "r") as f:
    lines = f.readlines()
    lines[1] = lines[1].replace("name", last_name)  # Replace "name" on the second line
    subject = lines[0].strip()
    message_body = "".join(lines[1:])

  # Create MIMEMultipart message
  message = MIMEMultipart()
  message["Subject"] = subject
  message["From"] = sender
  message["To"] = receiver

  # Attach message body
  message.attach(MIMEText(message_body, _charset="utf-8"))

  # Attach files if provided
  if attachment_paths:
    for attachment_path in attachment_paths:
      with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)  # Remove charset argument
        part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
        message.attach(part)

  # Send email with error handling
  try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
      server.starttls()
      server.login(sender, password)
      server.sendmail(sender, receiver, message.as_string())
      print(f" Message sent successfully to: {receiver}")
  except Exception as e:
    print(f" Error sending email: {e}")

def send_emails():
    """Reads data from JSON, sends personalized emails for each entry."""
    with open('extracted_data.json', 'r') as f:
        data = json.load(f)

    for entry in data:
        if 'Email' not in entry:
            raise ValueError(f" Missing email address for entry: {entry}")

        receiver = entry['Email']
        last_name = entry["Last_Name"]
        template_file = "file.txt"  # Default template

        # Optional logic for different templates based on last name
        send_personalized_email(receiver, last_name, template_file, attachment_paths=a)
#####to here......
def get_credentials():
    """Prompts the user for a username and password, and returns them as a tuple."""

    username = input(" Enter your username: ")
    password = input(" Enter your password: ")
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
    print(" Credentials saved successfully!")


def scan():

    floc = input(" Enter File Location of Json: ")
    gid = input(" Enter Google sheet ID: ")
    
    # Replace with the path to your service account key JSON file 
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    creds = ServiceAccountCredentials.from_json_keyfile_name(floc, SCOPES)

    # Authorize
    client = gspread.authorize(creds)

    # Replace with the ID of your Google Sheet 
    sheet_id = gid  # Replace with the actual ID

    # Open the sheet by ID
    sheet = client.open_by_key(sheet_id).sheet1

    # Get all data from the sheet
    data = sheet.get_all_values()

    # Assuming Last Name and Email are in columns with known positions (e.g., Last Name in column 2 and Email in column 3)
    last_name_column = 2  # Adjust this based on your actual column position
    email_column = 5  # Adjust this based on your actual column position

    # Create an empty list to store extracted data
    extracted_data = []

    # Skip the header row (assuming the first row contains column names)
    for row in data[1:]:
        last_name = row[last_name_column - 1]
        email = row[email_column - 1]
        # Create a dictionary to store Last Name and Email for each entry
        entry = {"Last_Name": last_name, "Email": email}
        extracted_data.append(entry)

    # Write the extracted data to a JSON file
    with open('extracted_data.json', 'w') as outfile:
        json.dump(extracted_data, outfile, indent=4)

    print(" Scan Completed!, extracted_data.json extracted done! ")





    





def main():
    wala()
    print(banner1)
    

    opt_butang = input(" Select Option [1-3]: ")

    if opt_butang == "1":
        aus = input(" [!] Are you sure you wanted to proceed? [y/n]: ")
        if aus == "y":
          print(" Starting......")
          send_emails()
          input("\n\n\n All Email Sent Successfully!, Press Enter to Go Menu....")
          main()
        elif aus == "n":
          print(" [+] Thanks God u change ur mind...")
          

        else:
          print(" [!] Incorrect Input!, pls try again.....")
          time.sleep(3)
          main()

    elif opt_butang == "2":
        print(" Scanning Data......")
        scan()
        input("\n\n\n Press Enter to Go Menu....")
        main()

        
    elif opt_butang == "3":
        print(op2)
        opt = input(" Select Option [1-3]: ")
        if opt == "1":
            username, password = get_credentials()
            save_credentials(username, password)
            input("\n\n Press Enter to Continue....")
            main()
            
        elif opt == "2":
            credentials = load_credentials()
            if credentials:
                username, password = credentials
                print(" Username:", username)
                print(" Password:", password)
            else:
                print(" No credentials found.")

            input("\n\n Press Enter to Continue....")
            main()
            


            
        elif opt == "3":
            removeacc()
            input("\n\n Press Enter to Continue....")
            main()
            
            
        else:
            input(" error pls select only [1-3]: ")
            main()

    elif opt_butang == "4":
        print(abt)
        input("\n\n Press Enter to Continue....")
        main()
        

    else:
        print(" error pls select only [1-3]")
        main()




        
    
main()
