#Bagas Satrio
#121140077
#Soal 1

# Class parent
class Komputer:
    # Atribut parent
    def __init__(self,nama, jenis, harga, merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk

# class turunan dari class Komputer
class Processor(Komputer):
    def __init__(self, merk, nama, harga, jumlah_core, kecepatan_processor):
        # Berfungsi untuk memanggil atribut dari class Parent
        super().__init__(nama, 'Processor', harga, merk)
        # Atribut anak
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor

# class turunan dari class komputer atau disebut class child
class RAM(Komputer):
   def __init__(self, merk, nama, harga, kapasitas_ram):
        # Berfungsi untuk memanggil atribut dari class Parent
        super().__init__(nama, "RAM", harga, merk)
        # Aribut anak
        self.kapasitas_ram = kapasitas_ram

# class turunan dari class komputer atau disebut class child
class HDD(Komputer):
    def __init__(self, merk, nama, harga, kapasitas_hdd, rpm):
        # Berfungsi untuk memanggil atribut dari class Parent
        super().__init__(nama, "SATA", harga, merk)
        # Aribut anak
        self.kapasitas_hdd = kapasitas_hdd
        self.rpm = rpm

# class turunan dari class komputer atau disebut class child
class VGA(Komputer):
    def __init__(self, merk, nama, harga, kapasitas_vga):
        # Berfungsi untuk memanggil atribut dari class Parent
        super().__init__(nama, "VGA", harga, merk)
        # Aribut anak
        self.kapasitasVGA = kapasitas_vga
    def __str__(self):
        return f"VGA {super().__str__()}"
# class turunan dari class komputer atau disebut class child
class PSU(Komputer):
    def __init__(self,merk,nama,harga,dayaPSU):
        # Berfungsi untuk memanggil atribut dari class Parent
        super().__init__(nama, "PSU", harga, merk)
        # Aribut anak
        self.dayaPSU = dayaPSU

# fungsi main
def main():
    # Objek
    p1 = Processor('Intel','Core i7 7740X',4350000,4,'4.3GHz')  
    p2 = Processor('AMD','Ryzen 5 3600',250000,4,'4.3GHz')
    ram1 = RAM('V-Gen','DDR4 SODimm PC19200/2400MHz',328000,'4GB')
    ram2 = RAM('G.SKILL','DDR4 2400MHz',328000,'4GB')
    hdd1 = HDD('Seagate','HDD 2.5 inch',295000,'500GB',7200)
    hdd2 = HDD('Seagate','HDD 2.5 inch',295000,'1000GB',7200)
    vga1 = VGA('Asus','VGA GTX 1050',250000,'2GB')
    vga2 = VGA('Asus','1060Ti',250000,'8GB')
    psu1 = PSU('Corsair','Corsair V550',250000,'500W')
    psu2 = PSU('Corsair','Corsair V550',250000,'500W')
    # Visualisasi list
    rakit_komputer_pertama = [p1, ram1, hdd1, vga1, psu1]
    # Menampilkan Komponen komputer berdasarkan list yang sudah dibuat
    print("Komputer 1")
    for rakit_komputer_pertama in rakit_komputer_pertama:
        print(f"{rakit_komputer_pertama.jenis} {rakit_komputer_pertama.nama} Produksi {rakit_komputer_pertama.merk}")

    # Visualisasi list
    rakit_komputer_kedua = [p2, ram2, hdd2, vga2, psu2]
    # Menampilkan Komponen komputer berdasarkan list yang sudah dibuat
    print("\nKomputer 2")
    for rakit_komputer_kedua in rakit_komputer_kedua:
        print(f"{rakit_komputer_kedua.jenis} {rakit_komputer_kedua.nama} Produksi {rakit_komputer_kedua.merk}")

# Untuk pengecekan fungsi main
if __name__ == "__main__":
    main()
