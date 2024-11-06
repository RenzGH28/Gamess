import random
import os
import pyfiglet
import requests
from colorama import Fore, Style, init

# Initialize colorama
init()

os.system('clear')
text727 = ("</===============================================================\>")
print(Fore.BLUE + text727)
text = pyfiglet.figlet_format("Tebak Kata")
print(Fore.YELLOW + text + Style.RESET_ALL)
print(Fore.BLUE + text727 + "\n")

def get_kata_list():
    url = "https://raw.githubusercontent.com/RenzGH28/Gamess/main/kataList.json"  # Ganti dengan URL file JSON Anda
    try:
        response = requests.get(url)
        response.raise_for_status()  # Akan melemparkan exception jika request gagal
        data = response.json()
        return [(item['kata'].lower(), item['clue']) for item in data]  # Mengambil kata dan clue
    except requests.RequestException as e:
        print(Fore.RED + f"Terjadi kesalahan saat mengakses file JSON: {e}" + Style.RESET_ALL)
        return []
    except ValueError:
        print(Fore.RED + "Format JSON tidak valid." + Style.RESET_ALL)
        return []

def play_game(kata_list):
    kata_rahasia, clue = random.choice(kata_list)
    tebakan = set()
    max_coba = 7
    gagal = 0

    print(Fore.YELLOW + "Game Ini Dibuat Oleh />RzDev404 Untuk Mengisi Kegabutannya.\n" + Style.RESET_ALL)
    print(Fore.CYAN + "Selamat datang di game Tebak Kata!" + Style.RESET_ALL)
    print(Fore.CYAN + f"Kata yang harus ditebak memiliki {len(kata_rahasia)} huruf." + Style.RESET_ALL)
    print(Fore.CYAN + f"Anda hanya memiliki {max_coba} kesempatan dalam menebak.\n\n" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + f"Petunjuk : {clue}\n\n" + Style.RESET_ALL)  # Menampilkan petunjuk

    while gagal < max_coba:
        display = [huruf if huruf in tebakan else "_" for huruf in kata_rahasia]
        print(" ".join(display))

        guess = input(Fore.YELLOW + "\nTebak huruf: " + Style.RESET_ALL).lower()

        # Validasi input
        if len(guess) != 1:
            print(Fore.RED + "Tolong masukkan hanya satu huruf." + Style.RESET_ALL)
            continue

        if guess in tebakan:
            print(Fore.YELLOW + "Anda sudah menebak huruf ini." + Style.RESET_ALL)
        elif guess in kata_rahasia:
            tebakan.add(guess)
            print(Fore.GREEN + "Tebakan benar!" + Style.RESET_ALL)
        else:
            gagal += 1
            print(Fore.RED + f"Tebakan salah! Anda memiliki {max_coba - gagal} kesempatan lagi." + Style.RESET_ALL)

        if set(kata_rahasia) == tebakan:
            print(Fore.GREEN + f"Selamat! Anda berhasil menebak kata '{kata_rahasia}'" + Style.RESET_ALL)
            break
    else:
        print(Fore.RED + f"Game Over! Kata yang benar adalah '{kata_rahasia}'." + Style.RESET_ALL)

def main():
    kata_list = get_kata_list()  # Ambil daftar kata dan clue dari file JSON
    if not kata_list:
        print(Fore.RED + "Tidak ada kata yang dapat digunakan untuk permainan." + Style.RESET_ALL)
        return

    while True:
        play_game(kata_list)
        # Pilihan untuk melanjutkan atau berhenti
        response = input(Fore.CYAN + "Ingin bermain lagi? \n(Y/" + Style.RESET_ALL + Fore.RED + "N" + Style.RESET_ALL + Fore.CYAN +"): " + Style.RESET_ALL).strip().lower()
        if response != "y":
            akhir = "Terima Kasih Telah Bermain!!"
            print(Fore.RED + akhir + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()