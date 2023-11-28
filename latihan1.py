# Dictionary
kontak = {"Ari": "081267888", "Dina": "087677776"}

# Menampilkan Kontak Ari
print("Kontak Ari:", kontak["Ari"], "\n")

# Menambahkan Kontak Riko dan Merubah Kontak Dina
kontak["Riko"] = "087654544"
kontak["Dina"] = "088999776"

# Menampilkan Semua Nama dan Nomor
print("Semua Nama:", kontak.keys())
print("Semua Nomor:", kontak.values(), "\n")

# Menampilkan semua daftar Nama dan Nomor
print("Daftar Nama dan Nomor:", list(kontak.items())[0:3], "\n")

# Menghapus Kontak Dina
del kontak["Dina"]
print("Setelah Menghapus Kontak Dina:", list(kontak.items())[0:3], "\n")
