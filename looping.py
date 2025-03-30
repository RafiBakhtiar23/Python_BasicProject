import sqlite3

conn = sqlite3.connect('identitas.db')
cursor = conn.cursor()

cursor.execute("""
  CREATE TABLE IF NOT EXISTS identitas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    umur INTEGER NOT NULL
  )
""")
conn.commit()

def tambah_identitas(nama, umur):
  cursor.execute("INSERT INTO identitas (nama, umur) VALUES (?, ?)", (nama, umur))
  conn.commit()
  print(f"Data dengan nama {nama} berhasil ditambahkan")
  
def tampilkan_identitas():
  cursor.execute("SELECT * FROM identitas")
  data = cursor.fetchall()
  for row in data:
    print(f"ID: {row[0]} | Nama: {row[1]} | Umur: {row[2]}")
  
def hapus_identitas(id_identitas):
  cursor.execute("DELETE FROM identitas WHERE id = ?", (id_identitas,))
  conn.commit()
  print(f"Data dengan ID {id_identitas} telah berhasil")
  
while True:
    print("\n=== MENU DATABASE PENGGUNA ===")
    print("1. Tambah Pengguna")
    print("2. Tampilkan Semua Pengguna")
    print("3. Hapus Pengguna")
    print("4. Keluar")
    
    pilihan = int(input("Pilih (1/2/3/4)"))
    
    if pilihan == 1:
      nama = input("Masukan nama : ")
      umur = int(input("Masukan umur : "))
      tambah_identitas(nama, umur)
    elif pilihan == 2:
      tampilkan_identitas()
    elif pilihan == 3:
      id_hapus = int(input("Masukan id yang akan di hapus : "))
      hapus_identitas(id_hapus)
    elif pilihan == 4:
      print("Program dikeluarkan")
      break
    else:
      print("Value eror, coba lagi")
      
    
    
    