#utils.py

def hitung_rata(n1, n2, n3):
     return (n1 + n2+n3) / 3

def status_lulus(rata):
  if rata > 75: 
    return "Lulus"
  else:
    return "Tidak Lulus"

def cari_tertinggi (data):
    return max(data, key=lambda x: x[hitung_rata'])

def cari terendah (data):
    return min(data, key-lambda x: x['rata'])

import utils
data mahasiswa []
jumlah int(input("Masukkan jumlah mahasiswa: "))
for i in range(Jumlah):
   print(f"\nData Mahasiswa ke-(1+1)")
   nama input("Nama: ")
   n1 float(input("Nilal 1: "))
   n2 float(input("Nilal 2: "))
   n3 float(input("Nilai 3: "))
   rata utils.hitung rata (n1, n2, n3)
   status utils.status lulus (rata)
   data_mahasiswa.append({
       "nama": nama,
       "nl": ni,
       "n2": n2,
       "n3": n3.
       "rata": rata,
       "status": status

print("\n Rekap Nilai Mahasiswa")
form in data mahasiswa:   
   print(f"[m[nama']) | Rata-rata: (n['rata']:.2f) | Status: (m['status']}")
tertinggi utils.cari_tertinggi (data_mahasiswa) terendah utils.cari_terendah(data_mahasiswa)
print("\ntahasiswa dengan nilai rata-rata tertinggi:") print(f"(tertinggi['nama']) | (tertinggi['rata']:.2f)")
print("\nMahasiswa dengan nilai rata-rata terendah:")
print (f"{terendah['nama']} | {terendah['rata']:.2f}")