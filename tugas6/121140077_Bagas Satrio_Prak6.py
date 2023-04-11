from abc import ABC, abstractmethod
import datetime

class AkunBank(ABC):
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo
    
    def lihatsaldo(self):
        print(f"Saldo {self.nama} saat ini adalah Rp {self.saldo}")
        
    @abstractmethod
    def transfer_saldo(self, jumlah):
        pass
    
    @abstractmethod
    def lihat_suku_bunga(self):
        pass

class AkunGold(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        
    def transfer_saldo(self, jumlah):
        usia_akun = datetime.date.today().year - self.tahun_daftar
        if jumlah < 100000:
            biaya_administrasi = 0
        elif usia_akun >= 3 and jumlah >= 100000:
            biaya_administrasi = 2000
        elif usia_akun < 3 and jumlah >= 100000:
            biaya_administrasi = 5000
        total_biaya = jumlah + biaya_administrasi
        if self.saldo < total_biaya:
            print("Maaf, saldo tidak cukup")
        else:
            self.saldo -= total_biaya
            print(f"Transfer Sebesar Rp. {jumlah} Sukses")
            print(f"Biaya administrasi Rp. {biaya_administrasi}")
            self.saldo -= total_biaya
    def lihat_suku_bunga(self):
        usia_akun = datetime.date.today().year - self.tahun_daftar
        if usia_akun >= 3 and self.saldo >= 1000000000:
            bunga = 0.01
        elif usia_akun < 3 and self.saldo >= 1000000000:
            bunga = 0.02
        else:
            bunga = 0.03
        print(f"Suku Bunga Bulanan {bunga*100}% per bulan")

class AkunSilver(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        
    def transfer_saldo(self, jumlah):
        usia_akun = datetime.date.today().year - self.tahun_daftar
        if jumlah < 100000:
            biaya_administrasi = 0
        elif usia_akun >= 3 and jumlah >= 100000:
            biaya_administrasi = 2000
        elif usia_akun < 3 and jumlah >= 100000:
            biaya_administrasi = 5000
        total_biaya = jumlah + biaya_administrasi
        if self.saldo < total_biaya:
            print("Maaf, saldo tidak cukup")
        else:
            self.saldo -= total_biaya
            print(f"Transfer Sebesar Rp. {jumlah} Sukses")
            print(f"Biaya administrasi Rp. {biaya_administrasi}")
            self.saldo -= total_biaya
    def lihat_suku_bunga(self):
        usia_akun = datetime.date.today().year - self.tahun_daftar
        if usia_akun >= 3 and self.saldo >= 10000000:
            bunga = 0.01
        elif usia_akun < 3 and self.saldo >= 10000000:
            bunga = 0.02
        else:
            bunga = 0.03
        print(f"Suku Bunga Bulanan {bunga*100}% per bulan")
                
data1 = AkunGold("Bagas Satrio", 2021, 10000000)
data1.lihatsaldo() 
data1.transfer_saldo(100000)
data1.lihatsaldo() 
data1.lihat_suku_bunga()

data2 = AkunSilver("Jokowi", 2020, 50000000)
data2.lihatsaldo()
data2.transfer_saldo(100000)
data2.lihatsaldo()
data2.lihat_suku_bunga()
