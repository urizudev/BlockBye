import psycopg2
import webbrowser
import bcrypt
import time
import os
import subprocess
from colorama import init, Fore

# Initialize colorama for colored text
init(autoreset=True)

# PostgreSQL connection parameters
db_params = {
    "dbname": "defaultdb",  # Replace with your actual database name
    "user": "avnadmin",
    "password": "AVNS_mdzAEY0UWIMYiOtIRKz",
    "host": "pg-2bf8ccc4-blockbye.aivencloud.com",
    "port": 16177,  # Replace with your PostgreSQL port
}

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(**db_params)
except psycopg2.OperationalError as e:
    print(Fore.RED + f"Error connecting to the database: {e}")
    exit(1)

# Create a cursor object
cursor = conn.cursor()

# Define the table name
table_name = 'users'

# Create the 'users' table if it doesn't exist
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
"""
cursor.execute(create_table_query)
conn.commit()

def clear_console():
    # Clear the console screen based on the platform (Windows or others)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



def main_menu():
    clear_console()
    print(Fore.BLUE + "  ____  _     ___   ____ _  ________   _______ ")
    print(Fore.BLUE + " | __ )| |   / _ \ / ___| |/ / __ ) \ / / ____|")
    print(Fore.BLUE + " |  _ \| |  | | | | |   | ' /|  _ \\ V /|  _|  ")
    print(Fore.BLUE + " | |_) | |__| |_| | |___| . \| |_) || | | |___ ")
    print(Fore.BLUE + " |____/|_____\___/ \____|_|\_\____/ |_| |_____|")
    print(Fore.GREEN + "Main Menu:")
    print("1. Installer")
    print("2. Exit")
    print("3. Bypass School dns")
    print("4. Chatroom")
def submenu():
    clear_console()
    print(Fore.BLUE + "  ____  _     ___   ____ _  ________   _______ ")
    print(Fore.BLUE + " | __ )| |   / _ \ / ___| |/ / __ ) \ / / ____|")
    print(Fore.BLUE + " |  _ \| |  | | | | |   | ' /|  _ \\ V /|  _|  ")
    print(Fore.BLUE + " | |_) | |__| |_| | |___| . \| |_) || | | |___ ")
    print(Fore.BLUE + " |____/|_____\___/ \____|_|\_\____/ |_| |_____|")
    print(Fore.BLUE + "Installer")
    print("1. Install Node Unblocker")
    print("2. Install Torrent")
    print("3. Install GTA: SA")
    print("9. Back to Main Menu")



def register_user(username, password):
    # Check if the username already exists
    check_user_query = f"SELECT * FROM {table_name} WHERE username = %s"
    cursor.execute(check_user_query, (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        return False  # Username already taken

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert the user into the database
    insert_user_query = f"INSERT INTO {table_name} (username, password) VALUES (%s, %s)"
    cursor.execute(insert_user_query, (username, hashed_password.decode('utf-8')))
    conn.commit()
    return True


def login_user(username, password):
    # Retrieve user data
    get_user_query = f"SELECT * FROM {table_name} WHERE username = %s"
    cursor.execute(get_user_query, (username,))
    user_data = cursor.fetchone()

    if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data[2].encode('utf-8')):  # Assuming password is in the third column
        return True  # Login successful
    else:
        return False  # Invalid username or password


def open_url_with_delay(url, delay_seconds):
    clear_console()
    print(Fore.YELLOW + f"Unblocking process started! Queue of {delay_seconds} seconds...")
    time.sleep(delay_seconds)
    webbrowser.open(url)

def install_node_unblocker():
    clear_console()
    repo_url = "https://github.com/urizudev/Node-Unblocker.git"
    install_directory = "Other"
    
    print(Fore.YELLOW + "Installing Node Unblocker...")
    
    # Clone the GitHub repository
    if os.system(f"git clone {repo_url} {install_directory}") == 0:
        print(Fore.GREEN + f"Node Unblocker installed successfully in the folder {install_directory}")
    else:
        print(Fore.RED + "Installation failed. Please make sure you have Git installed.")

def install_torrent():
    clear_console()
    repo_url = "https://github.com/urizudev/torrentsandutorent.git"
    install_directory = "Other/Program-Installers"
    
    print(Fore.YELLOW + "Installing uTorrent...")
    
    # Clone the GitHub repository
    if os.system(f"git clone {repo_url} {install_directory}") == 0:
        print(Fore.GREEN + f"uTorrent installed successfully in the folder {install_directory}")
    else:
        print(Fore.RED + "Installation failed. Please make sure you have Git installed.")

def install_sanandreas():
    clear_console()
    repo_url = "https://github.com/urizudev/gtasan.git"
    install_directory = "Other/gamez"
    
    print(Fore.YELLOW + "Installing GTA: SA...")
    
    # Clone the GitHub repository
    if os.system(f"git clone {repo_url} {install_directory}") == 0:
        print(Fore.GREEN + f"GTA: SA installed successfully in the folder {install_directory}")
    else:
        print(Fore.RED + "Installation failed. Please make sure you have Git installed.")

def main():
    # Implement login system
    logged_in = False  # Initialize to False
    username = None  # Initialize username

    while not logged_in:
        clear_console()
        print(Fore.BLUE + "  ____  _     ___   ____ _  ________   _______ ")
        print(Fore.BLUE + " | __ )| |   / _ \ / ___| |/ / __ ) \ / / ____|")
        print(Fore.BLUE + " |  _ \| |  | | | | |   | ' /|  _ \\ V /|  _|  ")
        print(Fore.BLUE + " | |_) | |__| |_| | |___| . \| |_) || | | |___ ")
        print(Fore.BLUE + " |____/|_____\___/ \____|_|\_\____/ |_| |_____|")
        print(Fore.MAGENTA + "                 Login")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if the username and password are valid
        logged_in = login_user(username, password)

        if logged_in:
            print(Fore.GREEN + "Login successful!\n")
        else:
            print(Fore.RED + "Invalid username or password. Please try again.")
            time.sleep(2)  # Pause for 2 seconds to show the message

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            submenu_choice = None
            while submenu_choice != '9':
                submenu()
                submenu_choice = input("Enter your choice: ")
                if submenu_choice == '1':
                    # Install Node Unblocker
                    install_node_unblocker()
                if submenu_choice == '2':
                    # Install torrent
                    install_torrent()
                if submenu_choice == '3':
                    install_sanandreas()  # Added parentheses to call the function
                elif submenu_choice == '9':
                    # Go back to the Main Menu
                    break
                else:
                    print(Fore.RED + "Invalid choice. Try again.")
                    time.sleep(1)  # Pause for 1 second to show the message
        elif choice == '2':
            print(Fore.GREEN + "Exiting the program.")
            break
        elif choice == '3':
            print(Fore.MAGENTA + "Connecting to dns...")
            delay_seconds = 3
            subprocess.run(["python", "startdns.py"])
            print(Fore.YELLOW + "Connected!")
            print(Fore.MAGENTA + "Connecting to proxy....")
            url = "http://unblock.hymac.xyz"
            delay_seconds = 3
            open_url_with_delay(url, delay_seconds) 
            subprocess.run(["python", "proxyconnect.py"], shell=True)
        elif choice == '4':
            print("Checking for erros")                 
            delay_seconds = 1
            print("No errors found! Starting...")
            subprocess.run(["python", "client.py"], shell=True)
        elif choice == '↨':
            secret()
            secret_choice = input("↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨")
            if secret_choice == '9':
                main_menu()
        else:
            print(Fore.RED + "Invalid choice. Try again.")
            time.sleep(1)  # Pause for 1 second to show the message

if __name__ == "__main__":
    main()

def secret():
    clear_console
    print(Fore.RED + "↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨↨")
    print(Fore.RED + "they found me")