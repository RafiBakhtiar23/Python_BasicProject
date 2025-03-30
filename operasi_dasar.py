angka1 = int(input("Masukan angka ke 1 : "))
operator = input("operator ( +, -, *, /, **, //, % ): ")
angka2 = int(input("Masukan angka ke 2 : "))

if operator == "+":
  hasil = angka1 + angka2
  print(f"Hasil penjumlahan dari {angka1} + {angka2} adalah {hasil}")

elif operator == "-":
  hasil = angka1 - angka2
  print(f"Hasil penjumlahan dari {angka1} - {angka2} adalah {hasil}")

elif operator == "*":
  hasil = angka1 * angka2
  print(f"Hasil penjumlahan dari {angka1} * {angka2} adalah {hasil}")

elif operator == "/":
  hasil = angka1 / angka2
  print(f"Hasil penjumlahan dari {angka1} / {angka2} adalah {hasil}")

elif operator == "**":
  hasil = angka1 ** angka2
  print(f"Hasil penjumlahan dari {angka1} ** {angka2} adalah {hasil}")

elif operator == "//":
  hasil = angka1 // angka2
  print(f"Hasil penjumlahan dari {angka1} // {angka2} adalah {hasil}")

elif operator == "%":
  hasil = angka1 % angka2
  print(f"Hasil penjumlahan dari {angka1} % {angka2} adalah {hasil}")
else:
  print("eror")