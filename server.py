import socket
import pyperclip
from win10toast import ToastNotifier
import sys


def getnetworkip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('<broadcast>', 0))  # sends a message to broadcast and waits for it to come back
    return s.getsockname()[0]


def server_start(ip):
    base_path = getattr(sys, '_MEIPASS', '.') + '/'  # pyinstaller compatibility for paths
    path = base_path + "custom.ico"
    toaster = ToastNotifier()  # toast message object
    my_ip = str(ip)
    # opens a socket listening on port 9797
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('', 9797)
    sock.bind(server_address)

    confirmation = 'received'  # confirmation message to send back
    last_recieved = ''  # avoids recieving the same message again
    while True:  # keep server open
        data, address = sock.recvfrom(4096)  # read incoming message and from what address
        if my_ip == address[0]:  # my message is rebroadcasted to me respond and continue
            sock.sendto(confirmation.encode(), address)
            continue
        else:  # i am getting a message from someone
            data = str(data.decode('UTF-8'))  # get the data
            if data != last_recieved:  # check if it is what i recieved before
                last_recieved = data
                pyperclip.copy(data)  # puts the new data directly into clipboard
                toaster.show_toast("LanClip Received", data, icon_path=path, duration=2)  # shows toast
            sock.sendto(confirmation.encode(), address)  # reply that data was received

