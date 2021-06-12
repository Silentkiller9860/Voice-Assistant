import socket
import subprocess
from win32com.client import Dispatch

def speak(s):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(s)


def ip():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print(f"The host name is : {host_name}")
    speak(f"The host name is : {host_name}")

    print(f"The host ip is : {host_ip}")
    speak(f"The host ip is : {host_ip}")
    

def wifi():
    devices = subprocess.check_output(['netsh','wlan','show','network'])
    devices = devices.decode('ascii')
    devices = devices.replace('\r','')
    print(f'These are avlaible networks : {devices}')
    speak(f'These are avlaible networks : {devices}')

# ip()
# wifi()