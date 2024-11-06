import os
from colorama import Fore, Style, init
import sys
import time
import pyfiglet

def slowprint(text, delay=0.1):  # Fungsi menerima dua argumen: text dan delay
    for char in text:
        sys.stdout.write(Fore.RED + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

os.system('clear')
text727 = ("</===========================================================\>")
print(Fore.BLUE + text727)
text = pyfiglet.figlet_format("  Menu Utama")
print(Fore.YELLOW + text + Style.RESET_ALL)
print(Fore.BLUE + text727 + "\n")
slowprint("Selamat Datang Di Halaman Utama\n", 0.05)

def menu_utama():
    print(Fore.CYAN + "1. Menu Game" + Style.RESET_ALL)
    print(Fore.CYAN + "2. Menu Spam" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Kembali" + Style.RESET_ALL)
    print(Fore.RED + "4. Keluar" + Style.RESET_ALL)

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == '1':
        menu_game()
    elif pilihan == '2':
        menu_spam()
    elif pilihan == '3':
        kembalisblm()
    elif pilihan == '4':
        print(Fore.YELLOW + "Terima kasih, sampai jumpa!" + Style.RESET_ALL)
    else:
        print("Pilihan tidak valid, coba lagi.")
        menu_utama()

def menu_game():
    os.system('python ./game/menu_game.py')

def kembalisblm():
    file_path = '/storage/emulated/0/Terminal Game/login.py'
    print(f"Running script: {file_path}")
    os.system(f'python "{file_path}"')

def menu_spam():
    print(Fore.RED + "Mohon Maaf Menu Ini Masih Dalam Tahap Pengembangan, Terimakasih" + Style.RESET_ALL)
    
if __name__ == '__main__':
    menu_utama()  