pertalite = "Pertalite"
pertamax = "Pertamax"
pertamax_turbo = "Pertamax Turbo"
solar = "Solar Subsidi"
dexlite = "Dexlite"
pertamax_dex = "Pertamax Dex"

print("|-------------Menu Bensin-------------|")
print("|1. Pertalite        10.000 / liter   |")
print("|2. Pertamax         12.500 / liter   |")
print("|3. Pertamax Turbo   13.700 / liter   |")
print("|4. Solar Subsidi    6.800 / liter    |")
print("|5. Dexlite          13.600 / liter   |")
print("|6. Pertamax Dex     13.900 / liter   |")
print("|-------------------------------------|")

nama = input("Masukan Nama : ")
jenis_bbm = int(input("Pilih Jenis BBM (1/2/3/4/5/6) : "))
jml_liter = int(input("Jumlah Liter : "))

if jenis_bbm == 1:
  total = 10.000 * jml_liter
  print("\033[1;36m|-------------------Hasil-------------------|\033[0m")
  print(f"\033[1;36mAtas nama {nama}\033[0m")
  print(f"\033[1;36mJenis bbm {pertalite} {jml_liter} liter\033[0m")
  print(f"\033[1;36mTotal pembayaran {total:.3f}\033[0m")
  print("\033[1;36m|-------------------------------------------|\033[0m")

elif jenis_bbm == 2:
  total = 12.500 * jml_liter
  print("\033[1;34m|-------------------Hasil-------------------|\033[0m")
  print(f"\033[1;34mAtas nama {nama}\033[0m")
  print(f"\033[1;34mJenis bbm {pertamax} {jml_liter} liter\033[0m")
  print(f"\033[1;34mTotal pembayaran {total:.3f}\033[0m")
  print("\033[1;34m|-------------------------------------------|\033[0m")

elif jenis_bbm == 3:
  total = 13.700 * jml_liter
  print("\033[1;36m|-------------------Hasil-------------------|\033[0m")
  print(f"\033[1;36mAtas nama {nama}\033[0m")
  print(f"\033[1;36mJenis bbm {pertamax_turbo} {jml_liter} liter\033[0m")
  print(f"\033[1;36mTotal pembayaran {total:.3f}\033[0m")
  print("\033[1;36m|-------------------------------------------|\033[0m")

elif jenis_bbm == 4:
  total = 6.800 * jml_liter
  print("\033[1;34m|-------------------Hasil-------------------|\033[0m")
  print(f"\033[1;34mAtas nama {nama}\033[0m")
  print(f"\033[1;34mJenis bbm {solar} {jml_liter} liter\033[0m")
  print(f"\033[1;34mTotal pembayaran {total:.3f}\033[0m")
  print("\033[1;34m|-------------------------------------------|\033[0m")

elif jenis_bbm == 5:
  total = 13.600 * jml_liter
  print("\033[1;36m|-------------------Hasil-------------------|\033[0m")
  print(f"\033[1;36mAtas nama {nama}\033[0m")
  print(f"\033[1;36mJenis bbm {dexlite} {jml_liter} liter\033[0m")
  print(f"\033[1;36mTotal pembayaran {total:.3f}\033[0m")
  print("\033[1;36m|-------------------------------------------|\033[0m")

elif jenis_bbm == 6:
  total = 13.900 * jml_liter
  print("\033[1;34m|-------------------Hasil-------------------|\033[0m")
  print(f"\033[1;34mAtas nama {nama}\033[0m")
  print(f"\033[1;34mJenis bbm {pertamax_dex} {jml_liter} liter\033[0m")
  print(f"\033[1;34mTotal pembayaran {total:.3f}\033[0m")
  print("\033[1;34m|-------------------------------------------|\033[0m")

else:
  print("Value Error")