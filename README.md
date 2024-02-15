## Mata Kuliah

Sebagai tugas praktikum: [6] Bahasa Pemrograman | Universitas Pelita Bangsa.

## Latihan 1

<p align="left">
  <img src="/ss/latihan1.jpg" width="450">
</p>

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

fungsi dan penjelasan sudah tertera pada **_#_** dan **_print_** diatas.
yang jelas **_keys_** dan **_values_** pada **_dictionary_** itu berhubungan.

## Praktikum 6

<p align="left">
  <img src="/ss/praktikum6.jpg" width="400">
  <img src="/ss/flowchart.jpg" width="360">
</p>

    def tambah_data(nim, nama, tugas, uts, uas, data_mahasiswa):
        # Menghitung nilai akhir berdasarkan bobot tugas, UTS, dan UAS
        nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
        # Menambahkan data mahasiswa ke dalam dictionary data_mahasiswa
        data_mahasiswa[nim] = {'Nama': nama, 'Nilai Akhir': nilai_akhir}
        # Menampilkan pesan bahwa data mahasiswa berhasil ditambahkan
        print(f"Data {nama} dengan NIM {nim} berhasil ditambahkan!")


    def ubah_data(nim, nama, tugas, uts, uas, data_mahasiswa):
        # Memeriksa apakah NIM ada dalam data_mahasiswa
        if nim in data_mahasiswa:
            # Menghitung nilai akhir berdasarkan bobot tugas, UTS, dan UAS
            nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
             Mengubah data mahasiswa dengan NIM tertentu
            data_mahasiswa[nim] = {'Nama': nama, 'Nilai Akhir': nilai_akhir}
            # Menampilkan pesan bahwa data mahasiswa berhasil diubah
            print(f"Data {nama} dengan NIM {nim} berhasil diubah!")
        else:
            # Menampilkan pesan bahwa NIM tidak ditemukan
            print(f"Data dengan NIM {nim} tidak ditemukan!")


    def hapus_data(nim, data_mahasiswa):
        # Memeriksa apakah NIM ada dalam data_mahasiswa
        if nim in data_mahasiswa:
            # Menghapus data mahasiswa dengan NIM tertentu
            del data_mahasiswa[nim]
            # Menampilkan pesan bahwa data mahasiswa berhasil dihapus
            print(f"Data dengan NIM {nim} berhasil dihapus!")
        else:
            # Menampilkan pesan bahwa NIM tidak ditemukan
            print(f"Data dengan NIM {nim} tidak ditemukan!")


    def tampilkan_data(data_mahasiswa):
        # Menampilkan header daftar nilai mahasiswa
        print("\nDaftar Nilai Mahasiswa:")
        print("{:<15} {:<25} {:<15}".format("NIM", "Nama", "Nilai Akhir"))
        print("-" * 60)
        # Menampilkan data nilai mahasiswa
        for nim, data in data_mahasiswa.items():
            print("{:<15} {:<25} {:<15}".format(nim, data['Nama'], data['Nilai Akhir']))


    def cari_data(nim, data_mahasiswa):
        # Memeriksa apakah NIM ada dalam data_mahasiswa
        if nim in data_mahasiswa:
            # Mendapatkan data mahasiswa dengan NIM tertentu
            data = data_mahasiswa[nim]
            # Menampilkan informasi data mahasiswa
            print(f"\nData dengan NIM {nim}:")
            print(f"Nama: {data['Nama']}")
            print(f"Nilai Akhir: {data['Nilai Akhir']}")
        else:
            # Menampilkan pesan bahwa NIM tidak ditemukan
            print(f"\nData dengan NIM {nim} tidak ditemukan!")


    def main():
        # Inisialisasi dictionary untuk menyimpan data mahasiswa
        data_mahasiswa = {}

        while True:
            # Menampilkan menu pilihan
            print("\nMenu Pilihan:")
            print("1. Tambah Data")
            print("2. Ubah Data")
            print("3. Hapus Data")
            print("4. Tampilkan Data")
            print("5. Cari Data")
            print("6. Keluar")

            # Meminta pengguna memilih menu
            pilihan = int(input("Pilih menu (1-6): "))

            # Melakukan aksi berdasarkan pilihan pengguna
            if pilihan == 1:
                # Meminta input data mahasiswa baru dan memanggil fungsi tambah_data
                nim = input("Masukkan NIM mahasiswa: ")
                nama = input("Masukkan nama mahasiswa: ")
                tugas = float(input("Masukkan nilai tugas: "))
                uts = float(input("Masukkan nilai UTS: "))
                uas = float(input("Masukkan nilai UAS: "))
                tambah_data(nim, nama, tugas, uts, uas, data_mahasiswa)
            elif pilihan == 2:
                # Meminta input data mahasiswa yang akan diubah dan memanggil fungsi ubah_data
                nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
                nama = input("Masukkan nama mahasiswa baru: ")
                tugas = float(input("Masukkan nilai tugas baru: "))
                uts = float(input("Masukkan nilai UTS baru: "))
                uas = float(input("Masukkan nilai UAS baru: "))
                ubah_data(nim, nama, tugas, uts, uas, data_mahasiswa)
            elif pilihan == 3:
                # Meminta input NIM mahasiswa yang akan dihapus dan memanggil fungsi hapus_data
                nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
                hapus_data(nim, data_mahasiswa)
            elif pilihan == 4:
                # Memanggil fungsi tampilkan_data
                tampilkan_data(data_mahasiswa)
            elif pilihan == 5:
                # Meminta input NIM mahasiswa yang akan dicari dan memanggil fungsi cari_data
                nim = input("Masukkan NIM mahasiswa yang akan dicari: ")
                cari_data(nim, data_mahasiswa)
            elif pilihan == 6:
                # Menampilkan pesan bahwa program selesai dan keluar dari loop
                print("Program selesai. Terima kasih!")
                break
            else:
                # Menampilkan pesan bahwa pilihan tidak valid
                print("Pilihan tidak valid. Silakan masukkan angka 1-6.")


    if __name__ == "__main__":
        # Memanggil fungsi main jika script dijalankan sebagai program utama
        main()

kode diatas menggunakan **_separate structure_** atau **_[]_** agar lebih mudah menempatkan **_value_**.
**_append_** berfungsi untuk menambahkan data ke list yang sudah ada.

## Documentation

All associated resources. are licensed under the [MIT License](https://mit-license.org/).
