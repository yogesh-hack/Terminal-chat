import socket, threading
from termcolor import colored
from pynput.keyboard import Key, Listener
import winsound
import getpass4

def on_press(key):
    if key == Key.enter:
        winsound.PlaySound("fo6bx-tesbj.wav", winsound.SND_ASYNC)

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False
# Collect events until released

print(f"""
    ___________                  .__              .__  _________ .__            __   
\__    ___/__________  _____ |__| ____ _____  |  | \_   ___ \|  |__ _____ _/  |_ 
  |    |_/ __ \_  __ \/     \|  |/    \\__  \ |  | /    \  \/|  |  \\__  \\   __\
  |    |\  ___/|  | \/  Y Y  \  |   |  \/ __ \|  |_\     \___|   Y  \/ __ \|  |  
  |____| \___  >__|  |__|_|  /__|___|  (____  /____/\______  /___|  (____  /__|  
             \/            \/        \/     \/             \/     \/     \/      
                           Made with ❤️ By yogesh
""")


nickname = getpass4.getpass("Enter your name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #socket initialization
client.connect(('127.0.0.1', 7976))                             #connecting client to server

def receive():
    while True:                                                 #making valid connection
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:                                                 #case on wrong ip/port details
            print("An error occured!")
            client.close()
            break
def write():
    while True:
        with Listener(
        on_press=on_press) as listener:
            message = "\033[96m{}\033[00m:\033[93m {}\033[00m".format(nickname, input(''))
            client.send(message.encode('ascii'))                                               #message layout
receive_thread = threading.Thread(target=receive)               #receiving multiple messages
receive_thread.start()
write_thread = threading.Thread(target=write)                  #sending messages 
write_thread.start()


