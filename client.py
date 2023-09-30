import socket
import threading
import json
import os
import subprocess
import webbrowser
from colorama import init, Fore

from main import clear_console

def idk():
    clear_console()
    print(Fore.YELLOW + f"Starting uwu")
    
    url = "https://blockbyechats.urizu.repl.co/"
    webbrowser.open(url)


def enter_server():
    os.system('cls||clear')
    with open('servers.json') as f:
        data = json.load(f)
    print('Your servers: ', end="")
    for server in data:
        print(server, end=" ")
    print(Fore.BLUE + "  ____  _     ___   ____ _  ________   _______ ")
    print(Fore.BLUE + " | __ )| |   / _ \ / ___| |/ / __ ) \ / / ____|")
    print(Fore.BLUE + " |  _ \| |  | | | | |   | ' /|  _ \\ V /|  _|  ")
    print(Fore.BLUE + " | |_) | |__| |_| | |___| . \| |_) || | | |___ ")
    print(Fore.BLUE + " |____/|_____\___/ \____|_|\_\____/ |_| |_____|")
    print(Fore.MAGENTA + "                 Chats")
    server_name = input("\nEnter the server name:")
    global nickname
    global password
    nickname = input("Choose Your Nickname:")
    if nickname == 'admin':
        password = input("Enter Password for Admin:")

    ip = data[server_name]["ip"]
    port = data[server_name]["port"]
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

def add_server():
    os.system('cls||clear')
    print(Fore.BLUE + "  ____  _     ___   ____ _  ________   _______ ")
    print(Fore.BLUE + " | __ )| |   / _ \ / ___| |/ / __ ) \ / / ____|")
    print(Fore.BLUE + " |  _ \| |  | | | | |   | ' /|  _ \\ V /|  _|  ")
    print(Fore.BLUE + " | |_) | |__| |_| | |___| . \| |_) || | | |___ ")
    print(Fore.BLUE + " |____/|_____\___/ \____|_|\_\____/ |_| |_____|")
    print(Fore.MAGENTA + "                 Chats / Add Server")
    server_name = input("Enter a name for the server:")
    server_ip = input("Enter the IP address of the server:")
    server_port = int(input("Enter the port number of the server:"))

    with open('servers.json', 'r') as f:
        data = json.load(f)

    with open('servers.json', 'w') as f:
        data[server_name] = {"ip": server_ip, "port": server_port}
        json.dump(data, f, indent=4)

stop_thread = False

def receive():
    global stop_thread
    while True:
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
                next_message = client.recv(1024).decode('ascii')
                if next_message == 'PASS':
                    client.send(password.encode('ascii'))
                    response = client.recv(1024).decode('ascii')
                    if response == 'REFUSE':
                        print("Connection is Refused !! Wrong Password")
                        stop_thread = True
                    elif response == 'ACCEPT':
                        print("Password accepted. You are now connected to the server.")
                elif next_message == 'BAN':
                    print('Connection Refused due to Ban')
                    client.close()
                    stop_thread = True
            else:
                print(message)
        except socket.error:
            print('Error Occurred while Connecting')
            client.close()
            stop_thread = True

def write():
    global stop_thread
    while True:
        if stop_thread:
            break
        message = input("")
        if message.startswith('/'):
            if nickname == 'admin':
                if message.startswith('/kick'):
                    client.send(f'KICK {message[6:]}'.encode('ascii'))
                elif message.startswith('/ban'):
                    client.send(f'BAN {message[5:]}'.encode('ascii'))
                if message.startswith('/help'):
                    print("Help commands!")
                    print("/ban - ban")
                    print("/kick - kick")
            else:
                print("Commands can be executed by Admins only !!")
        else:
            if message.startswith('>'):
                formatted_message = f'\033[32m{message[1:]}\033[0m'  # Green text
            elif message.startswith('p>'):
                formatted_message = f'\033[35m{message[2:]}\033[0m'  # Purple text
            else:
                formatted_message = message  # Normal text

            client.send(f'{nickname}: {formatted_message}'.encode('ascii'))

# Menu loop, it will loop until the user chooses to enter a server
while True:
    os.system('cls||clear')
    print(Fore.BLUE + "  ____  _     ___   ____ _  ________   _______ ")
    print(Fore.BLUE + " | __ )| |   / _ \ / ___| |/ / __ ) \ / / ____|")
    print(Fore.BLUE + " |  _ \| |  | | | | |   | ' /|  _ \\ V /|  _|  ")
    print(Fore.BLUE + " | |_) | |__| |_| | |___| . \| |_) || | | |___ ")
    print(Fore.BLUE + " |____/|_____\___/ \____|_|\_\____/ |_| |_____|")
    print(Fore.MAGENTA + "                 Chats")
    option = input("(1)Enter server (2)Add server (3)Online servers ")
    if option == '1':
        enter_server()
        break
    elif option == '2':
        add_server()
    elif option == '3':
        idk() 
        subprocess.run(["python", "startdns.py"])
        subprocess.run(["python"], "proxyconnect.py")

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
