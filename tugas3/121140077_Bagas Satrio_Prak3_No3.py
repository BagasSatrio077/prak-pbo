#Bagas Satrio
#121140077

class Baju:
    # atribut kelas (nilai konsisten untuk semua instance)
    jenis = "kaos"
    ukuran = "M"

    def __init__(self, harga, warna):
        # atribut instance (nilai berbeda untuk setiap instance)
        self.harga = harga
        # atribut private (hanya bisa diakses di dalam kelas)
        self.__warna = warna

    def cek_stok(self):
        print("Stok tersedia")
    
    def diskon(self):
        # atribut public (bisa diakses di luar kelas)
        self.harga *= 0.5
        print("Harga Setelah Diskon :",self.harga)
    def __cek_ukuran(self):
        # atribut private (hanya bisa diakses di dalam kelas)
        print("Ukuran : " + self.ukuran)
    
    def pesan(self):
        # memanggil fungsi private di dalam kelas
        self.__cek_ukuran()
        print("Baju dengan warna " + self.__warna + " telah dipesan")
    
# membuat objek baju1 dan baju2 dari kelas Baju
baju1 = Baju(100000, "Hitam")
baju2 = Baju(150000, "Merah")

# memanggil atribut dan fungsi public di luar kelas
# Akan menghasilkan output Harga Baju Senilai 100000
print("Harga Sebelum Diskon :", baju1.harga)
# Harga 100000 akan dikali dengan diskon sebesar 50% atau 0.5
baju1.diskon()
# Sehingga akan membuat output Harga Baju menjadi 50000
# Output ukuran baju
baju1.cek_stok()
# Output informasi baju yang dipesan
baju1.pesan()
