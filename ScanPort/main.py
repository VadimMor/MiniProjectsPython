import argparse
from colorama import init, Fore
from socket import *

init()
GREEN = Fore.GREEN
RED = Fore.RED


# Checking the socket type
def checkType(ip, ports, isTcp, isUdp):
    for port in range(int(ports[0]), int(ports[1])+1):
        if isTcp and isUdp:
            scanTcp(ip, port)
            scanUdp(ip, port)
        elif isUdp:
            scanUdp(ip, port)
        else:
            scanTcp(ip, port)


# Tcp socket scanning
def scanTcp(ip, port):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((ip, port))
        print(f"{GREEN}[+] Port:{port} tcp OPEN")

    except:
        print(f"{RED}[+] Port:{port} tcp CLOSED")

    finally:
        sock.close()


# Udp socket scanning
def scanUdp(ip, port):
    try:
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.connect((ip, port))
        print(f"{GREEN}[+] Port:{port} udp OPEN")

    except:
        print(f"{RED}[+] Port:{port} udp CLOSED")

    finally:
        sock.close()


# Based function
def main():
    print("Сканер портов\n")
    try:
        parser = argparse.ArgumentParser("Scanner port")
        parser.add_argument("-a", "--address", type=str, help="Введите ip адрес для сканирования")
        parser.add_argument("-p", "--port", type=str, help="Введите сканируемые порты")
        parser.add_argument("-sT", "--tcp", action="store_true")
        parser.add_argument("-sU", "--udp", action="store_true")
        args = parser.parse_args()
        checkType(args.address,
                  args.port.split("-"),
                  args.tcp,
                  args.udp)
        
    except:
        print("Не указаны аргументы\n Пример: python ./server.py  -p 130-137 -a ru.wikipedia.org")

# Start
main()