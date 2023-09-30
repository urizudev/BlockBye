from colorama import init, Fore
import socket

#HELO :dd)000ASDFGHKSDFHLJKASHDF

proxy_host = "127.0.0.1"
proxy_port = 8888

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((proxy_host, proxy_port))

    print(Fore.YELLOW + "CONNECTED HAVE FUNZZ >-< HAGHHGHKLASLD'JLHAGSDF ABASHKDGFJFA ILY KIDDOS")

    while True:
        pass

if __name__ == "__main__":
    main()
