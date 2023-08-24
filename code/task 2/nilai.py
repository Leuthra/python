# input digunakan untuk memasukan data
nama = input("nama siswa: ")
nilai = int(input(f"nilai siswa {nama}: "))

# Membuat kondisi yang sesuai
if nilai >= 80:
    keterangan = "Lulus"
else:
    keterangan = "Remedial"

# output yang dihasilkan 
print(f"Nama: {nama}")
print(f"Nilai: {nilai}")
print(f"Keterangan: {keterangan}")
