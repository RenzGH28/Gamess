import os
from colorama import Fore, Style, init
import sys
import time
import pyfiglet
import requests

# URL file menu_game di GitHub
MENU_GAME_URL = 'https://raw.githubusercontent.com/RenzGH28/Gamess/main/game/menu_game.py'

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

# Fungsi untuk Menu Game
def menu_game():
    try:
        response = requests.get(MENU_GAME_URL)
        response.raise_for_status()  # Memastikan tidak ada error pada response
        exec(response.text)  # Jalankan kode Python dari URL
    except requests.exceptions.RequestException as e:
        print(f"Gagal mengambil atau menjalankan file dari URL: {e}")

# Menu Utama yang memanggil fungsi menu_game
def menu_utama():
    print(Fore.CYAN + "1. Menu Game" + Style.RESET_ALL)
    print(Fore.CYAN + "2. Menu Spam" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Kembali" + Style.RESET_ALL)
    print(Fore.RED + "4. Keluar" + Style.RESET_ALL)

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == '1':
        menu_game()  # Panggil menu_game() dengan definisi yang jelas
    elif pilihan == '2':
        menu_spam()
    elif pilihan == '3':
        kembalisblm()
    elif pilihan == '4':
        print(Fore.YELLOW + "Terima kasih, sampai jumpa!" + Style.RESET_ALL)
    else:
        print("Pilihan tidak valid, coba lagi.")
        menu_utama()

# Fungsi untuk opsi kembali ke halaman login
def kembalisblm():
    file_path = '/storage/emulated/0/Terminal Game/login.py'
    print(f"Running script: {file_path}")
    os.system(f'python "{file_path}"')

# Fungsi placeholder untuk menu spam
def menu_spam():
    print(Fore.RED + "Mohon Maaf Menu Ini Masih Dalam Tahap Pengembangan, Terimakasih" + Style.RESET_ALL)
    
# Jalankan program utama
if __name__ == '__main__':
    menu_utama()
