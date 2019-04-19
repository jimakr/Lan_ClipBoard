from win10toast import ToastNotifier
import pyperclip
import _thread
import keyboard
from server import server_start, getnetworkip
from client import send_clipboard
import sys


# pyinstaller compatibility to work with paths in included icon files
base_path = getattr(sys, '_MEIPASS', '.') + '/'
path = base_path + "custom.ico"  # custom ico for notification
ip = getnetworkip()  # gets the computers ip


def copysend():  # function that runs the client to send a message
    send_clipboard(ip)  # client call
    toaster.show_toast("LanClip Send", pyperclip.paste(), icon_path=path, duration=2)  # displays toast notification


toaster = ToastNotifier()  # toast notification handler
_thread.start_new(server_start, ( ip, ))  # start a listening server for incoming messages in a new thread
toaster.show_toast("LanClip Started", "Share text in clipboard", icon_path=path, duration=2)
keyboard.add_hotkey('windows+c', copysend)  # binds windows key + c to a shortcut for sending clipboard contents
keyboard.wait('ctrl+e')  # exit shortcut program will wait for this before terminating
toaster.show_toast("LanClip Closing", "Goodbye!", icon_path=path, duration=2)
