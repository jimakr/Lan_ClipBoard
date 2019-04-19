from socket import *
import pyperclip


def send_clipboard(myip):
    # Create a UDP socket
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    sock.settimeout(0.5)  # timeout between send and respond to determine failure and resend
    # it is so low because udp over wifi is lossy and we need to send the same message many times

    # using the following address the message is broadcasted to every device
    server_address = ('255.255.255.255', 9797)
    message = pyperclip.paste()  # clipboard contents

    try:  # try to open the connection and sent data
        while True:
            try:
                sock.sendto(message.encode(), server_address)  # sends message to everybody
                while True:
                    data, server = sock.recvfrom(4096)  # retrieves response from someone
                    print(server[0])  # for debugging lossy messages in console

                    if myip != server[0]:  # check if i responded to my message or someone else
                        break  # if it got to the other person it's ok

            except:  # handles error from timeout, its time to send again
                print("noise in network packet lost error")

            if myip != server[0]:  # same but for the outer loop to end broadcast
                break
    finally:
        sock.close()  # closes connection


