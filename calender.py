import calendar

year = int(input("Masukan Tahun : "))
while True:
  m = int(input("Pilih Bulan : "))
  print("\n")
  
  if m == 1:
    print(calendar.month(year, m))
  elif m == 2:
    print(calendar.month(year, m))
  elif m == 3:
    print(calendar.month(year, m))
  elif m == 4:
    print(calendar.month(year, m))
  elif m == 5:
    print(calendar.month(year, m))
  elif m == 6:
    print(calendar.month(year, m))
  elif m == 7:
    print(calendar.month(year, m))
  elif m == 8:
    print(calendar.month(year, m))
  elif m == 9:
    print(calendar.month(year, m))
  elif m == 10:
    print(calendar.month(year, m))
  elif m == 11:
    print(calendar.month(year, m))
  elif m == 12:
    print(calendar.month(year, m))
  else:
    print("Error")
    