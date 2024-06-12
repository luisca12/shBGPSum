import os
from commandsCLI import shBGPSum

def greetingString():
        os.system("CLS")
        print('  ------------------------------------------------- ')
        print("    Welcome to the automated remove ACE program ")
        print('  ------------------------------------------------- ')

def menuString(deviceIP, username):
        os.system("CLS")
        print(f"Connected to: {deviceIP} as {username}\n")
        print('  -------------------------------------------------------------- ')
        print('\t\tMenu - Please choose an option')
        print('\t\t  Only numbers are accepted')
        print('  -------------------------------------------------------------- ')
        print('  >\t\t1. To run the following commands:\t       <\n')
        print(f'\t\t\t{shBGPSum}    ')      
        print('  >\t\t\t2. Exit the program\t\t       <')
        print('  -------------------------------------------------------------- \n')

def inputErrorString():
        os.system("CLS")
        print('  ------------------------------------------------- ')  
        print('>      INPUT ERROR: Only numbers are allowed       <')
        print('  ------------------------------------------------- ')

def shRunString(validIPs):
        print('  ------------------------------------------------- ')  
        print(f'> Taking a show run of the device {validIPs} <')
        print('>\t   Please wait until it finishes\t  <')
        print('  ------------------------------------------------- ')
