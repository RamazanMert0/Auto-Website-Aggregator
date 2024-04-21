# Coded By LordSUCCESS | https://www.turkhackteam.org/uye/lordsuccess.1014976/
# Kullanırken Proxy Yazılımı Kullanmazınızı Öneririm

from googlesearch import search
from colorama import Fore
from time import sleep
from os import system
import platform
import requests

def baslat():
    osname = platform.system()
    if osname == "Windows":
        system("cls")
    elif osname == "Linux":
        system("clear")

    banner = (Fore.BLUE + "    #                                #     #                                                ######                                     \n" +
          "   # #    #    #  #####   ####       #  #  #  ######  #####    ####   #  #####  ######      #     #  #   ####   #    #  ######  #####  \n" +
          "  #   #   #    #    #    #    #      #  #  #  #       #    #  #       #    #    #           #     #  #  #    #  #   #   #       #    # \n" +
          " #     #  #    #    #    #    #      #  #  #  #####   #####    ####   #    #    #####       ######   #  #       ####    #####   #    # \n" +
          " #######  #    #    #    #    #      #  #  #  #       #    #       #  #    #    #           #        #  #       #  #    #       #####  \n" +
          " #     #  #    #    #    #    #      #  #  #  #       #    #  #    #  #    #    #           #        #  #    #  #   #   #       #   #  \n" +
          " #     #   ####     #     ####        ## ##   ######  #####    ####   #    #    ######      #        #   ####   #    #  ######  #    # \n" +
          "Coded By LordSUCCESS\n" + 
          Fore.RESET)
    print(banner)

baslat()
proxys = "http://69.84.182.43:80"

try:
    dork = input(Fore.GREEN + "Dork Girin: " + Fore.RESET)
    site_sayisi = input(Fore.GREEN + "Kaç Site Çıkması Gerek: " + Fore.RESET)
    for url in search(dork, num_results=int(site_sayisi), proxy=proxys, lang="tr"):
        print(url)
        sleep(2)
except requests.exceptions.HTTPError as e:
    print(Fore.RED + f"{e}" + Fore.RESET)
    print(Fore.RED + "İstek Hatası, Exploit Kapatılıyor..." + Fore.RESET)
    sleep(2)
except ValueError as e:
    print(Fore.RED + "Karakter Hatası, Exploit Kapatılıyor..." + Fore.RESET)
    sleep(2)