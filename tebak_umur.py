import random

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

umur_rafi = random.randint(12, 20) 

print(f"{CYAN}Selamat datang di game Tebak Umur Rafi! 🎉{RESET}")
print(f"{YELLOW}Coba tebak umur Rafi antara 12 hingga 20 tahun.{RESET}")

while True:
    try:
        tebakan = int(input("Masukkan tebakanmu: "))

        if tebakan < umur_rafi:
            print(f"{RED}Terlalu rendah! Coba lagi.{RESET}")
        elif tebakan > umur_rafi:
            print(f"{RED}Terlalu tinggi! Coba lagi.{RESET}")
        else:
            print(f"{GREEN}Selamat! Kamu benar, umur Rafi adalah {umur_rafi} tahun! 🎉{RESET}")
            break
    except ValueError:
        print(f"{RED}Masukkan angka yang valid!{RESET}")
