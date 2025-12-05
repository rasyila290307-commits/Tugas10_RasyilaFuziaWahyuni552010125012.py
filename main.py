#main.py

import utils
def main():
    """"
    Program utama:
    - Input jumlah mahasiswa
    - Input data per mahasiswa
    - Hitung rata-rata
    - Tentukan status
    - Simpan ke list
    - Tampilkan hasil
    """
data_mahasiswa = []
jumlah = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah):
    print(f"\nData mahasiswa ke-(i+1)")

    mhs = utils.input_mahasiswa()
    rata = utils.hitung_rata(mhs["nilai"])  
    status = utils.tentukan_status(rata)

    mhs["rata"] = rata
    mhs["status"] = status

    data_mahasiswa.append(mhs)
    utils.tampilkan_hasil(data_mahasiswa)

if __name__ =="__main__":
    main()
