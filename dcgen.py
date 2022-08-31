import requests
import random
import string
import time
import os
import threading
from  colorama import Fore,Back,Style
from  colorama import init
def fortnite():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system(f"title V2")
    print(Fore.BLUE +'''
 ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
 ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒ 
░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
         ░  ░              ░         ░ ░                  ░ ░      ░ ░      ░  ░
 ------------------------------------------------------------------------------
                            https://discord.gg/hNu2Ea3An4                                                                                                                                                                                                                                                                                                                                
                                                    ''')
    time.sleep(2)
    print(Fore.BLUE + 'Made by lem#3072')
    time.sleep(0.3)
    print(Fore.BLUE + 'Download more tools in our Discord!\n')
    time.sleep(0.2)

    num = int(input("\033[36;40m" + 'How many codes do u want to generate and check -> '))
    print("\033[m")

    with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
        print(Fore.BLUE + 'Codes will be Generated, pls wait!')

        start = time.time()

        for i in range(num):
            code = "".join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k=16
            ))

            file.write(f'{code}\n')

        print(Fore.BLUE + f'Generated {num} codes | Time taken: {time.time() - start}\n')
    count = 0
    with open("Nitro Codes.txt") as file:
        for line in file.readlines():
            nitro = line.strip("\n")

            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

            r = requests.get(url)

            if r.status_code == 200:
                print(Fore.GREEN + f' [Valid] | {nitro} ',  r.status_code)
                break
            else:
                count +=1
                print(Fore.RED + f' [Invalid] | {nitro}  CHECKED CODES: {count}   STATUS CODE : {r.status_code} ' ,end='\r')

    input("\033[36;40m" + "\nDone! Valid codes are in Valid Codes.txt!")

loading_process = threading.Thread(target=fortnite)
loading_process.start()
loading_process.join()