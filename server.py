import socket
import pyperclip
from win10toast import ToastNotifier
import sys


def server_start():
    base_path = getattr(sys, '_MEIPASS', '.') + '/'  # pyinstaller compatibility for paths
    path = base_path + "custom.ico"
    toaster = ToastNotifier()  # toast message object

    # opens a socket listening on port 9797
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('', 9797)
    sock.bind(server_address)

    confirmation = 'received'  # confirmation message to send back

    while True:  # keep server open
        data, address = sock.recvfrom(4096)  # read incoming message and from what address
        data = str(data.decode('UTF-8'))
        pyperclip.copy(data)  # puts the new data directly into clipboard
        toaster.show_toast("LanClip Received", data, icon_path=path, duration=2)  # shows toast
        sock.sendto(confirmation.encode(), address)  # reply that data was received

