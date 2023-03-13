#Bagas Satrio
#121140077

# Membuat class AkunBank
class AkunBank:
    # Konstruktor
    list_pelanggan = []

    def __init__(self, no, nama, saldo):
        self.__no_pelanggan = no
        self.__nama_pelanggan = nama
        self.__jumlah_saldo = saldo
        AkunBank.list_pelanggan.append(self)
    def lihat_menu(self):
            print("Selamat datang di Bank Mager")
            print(f"Halo {self.__nama_pelanggan}, Ada yang bisa kami bantu ?")
            print("1. Lihat Saldo \n2. Tarik tunai \n3. Transfer Uang \n4. Keluar")
    # Melihat Saldo
    def lihat_saldo(self):
        print(f"{self.__nama_pelanggan} memiliki saldo {self.__jumlah_saldo}")

    # Tarik Tunai
    def tarik_tunai(self):
        jumlah_tarik = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
        if jumlah_tarik > self.__jumlah_saldo:
            print("Nominal saldo yang Anda punya tidak cukup!")
        else:
            self.__jumlah_saldo -= jumlah_tarik
            print("Saldo berhasil ditarik!")
            
    # Transfer
    def transfer(self):
        nominal = int(input("Masukkan jumlah nominal yang ingin ditransfer  : "))
        norek = int(input(f"No rekening tujuan : "))
        tujuan = None
        for pelanggan in AkunBank.list_pelanggan:
            if pelanggan.__no_pelanggan == norek:
                tujuan = pelanggan
                break
        if tujuan is None:
            print("No rekening tujuan tidak dikenal! Kembali ke menu utama")
        else:
            if nominal > self.__jumlah_saldo:
                print("Saldo tidak mencukupi untuk transfer!")
            else:
                self.__jumlah_saldo -= nominal
                tujuan.__jumlah_saldo += nominal
                print(f"Transfer Rp {nominal} ke {tujuan._AkunBank__nama_pelanggan} sukses!")
                
# Inisialisasi
Akun1 = AkunBank(123, "Bagas", 1000000)
Akun2 = AkunBank(456, "Ibra", 2000000)
Akun3 = AkunBank(789, "Agung", 3000000)
Akun1.lihat_menu()
nomor_input = int(input("Pilih kebutuhan( 1 / 2 / 3 / 4 ) : "))
while nomor_input != 4:
    if nomor_input == 1:
        Akun1.lihat_saldo()
    elif nomor_input == 2:
        Akun1.tarik_tunai()
    elif nomor_input == 3:
        Akun1.transfer()
    else:
        print("Input tidak valid!")
    Akun1.lihat_menu()
    nomor_input = int(input("Masukkan Nomor : "))

print("Terima kasih!")
