import os
from colorama import Fore, Style, init
import sys
import time
import pyfiglet
import requests

# URL file game di GitHub
TEBAK_ANGKA_URL = 'https://raw.githubusercontent.com/RenzGH28/Gamess/main/game/tebak%20angka.py'
TEBAK_KATA_URL = 'https://raw.githubusercontent.com/RenzGH28/Gamess/main/game/tebak%20kata.py'

def slowprint(text, delay=0.1):  # Fungsi menerima dua argumen: text dan delay
    for char in text:
        sys.stdout.write(Fore.RED + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)

os.system('clear')
text727 = ("</===========================================================\>")
print(Fore.BLUE + text727)
text = pyfiglet.figlet_format("    Menu Game")
print(Fore.YELLOW + text + Style.RESET_ALL)
print(Fore.BLUE + text727 + "\n")
slowprint("Selamat Datang Di Halaman Game\n", 0.05)

def menu_utama():
    print(Fore.CYAN + "1. Tebak Kata" + Style.RESET_ALL)
    print(Fore.CYAN + "2. Tebak Angka" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Kembali" + Style.RESET_ALL)
    print(Fore.RED + "4. Keluar" + Style.RESET_ALL)

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == '1':
        run_from_url(TEBAK_KATA_URL)
    elif pilihan == '2':
        run_from_url(TEBAK_ANGKA_URL)
    elif pilihan == '3':
        kembalisblm()
    elif pilihan == '4':
        print(Fore.YELLOW + "Terima kasih, sampai jumpa!" + Style.RESET_ALL)
    else:
        print("Pilihan tidak valid, coba lagi.")
        menu_utama()

def run_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Periksa jika ada error pada respons
        exec(response.text)  # Jalankan kode dari URL sebagai Python
    except requests.exceptions.RequestException as e:
        print(f"Gagal mengambil atau menjalankan file dari URL: {e}")

def kembalisblm():
    file_path = '/storage/emulated/0/Terminal Game/src/menu_utama.py'
    print(f"Running script: {file_path}")
    os.system(f'python "{file_path}"')

if __name__ == '__main__':
    menu_utama()
