from socket import *
import pyperclip


def send_clipboard():
    # Create a UDP socket
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    sock.settimeout(5)
    # using the following address the message is broadcasted to every device
    server_address = ('255.255.255.255', 9797)
    message = pyperclip.paste()  # clipboard contents

    try:
        while True:
            sock.sendto(message.encode(), server_address)  # sends message
            data, server = sock.recvfrom(4096)  # retrieves response

            if data.decode('UTF-8') == 'received':  # confirms message sent
                break  # stop trying
            else:
                print('wrong server')  # error message
    finally:
        sock.close()  # closes connection


