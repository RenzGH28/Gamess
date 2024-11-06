import random
import pyfiglet
import os
import pyfiglet

os.system('clear')
text = pyfiglet.figlet_format("Tebak Angka")
print (text)
def main():
    print("Selamat datang di game Tebak Angka!")
    print("Saya sudah memilih angka antara 1 hingga 100.\n")
    print("Silakan Tebak Angkanya Dalam 7× Percobaan.\n")
    
    # Pilih angka acak antara 1 dan 100
    angka_rahasia = random.randint(1, 100)
    percobaan = 0
    max_percobaan = 7

    # Looping untuk memberi kesempatan menebak
    while percobaan < max_percobaan:
        tebak = int(input(f"Percobaan {percobaan + 1}: Masukkan tebakan Anda: "))
        percobaan += 1
        
        if tebak < angka_rahasia:
            print("Angka terlalu kecil!")
        elif tebak > angka_rahasia:
            print("Angka terlalu besar!")
        else:
            print(f"Selamat! Anda menebak dengan benar dalam {percobaan} percobaan.")
            break
    
    if tebak != angka_rahasia:
        print(f"Sayang sekali, Anda gagal. Angka yang benar adalah {angka_rahasia}.")

if __name__ == "__main__":
    main()

