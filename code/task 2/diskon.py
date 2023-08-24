print("===================================")
print("========= Selamat Datang ==========")
print("===================================")
# input untuk memasukan data
tinggi = float(input("Masukkan tinggi anak (dalam cm): "))
# float nilai desimal 
umur = int(input("Masukkan umur anak (dalam tahun): "))
# int nilai bulat

# kondisi umur dan tinggi memperngaruhi harga tiket
if tinggi >= 100 and umur >= 2:
    keterangan = "Harga Normal"
elif tinggi >= 80 and umur >= 2:
    keterangan = "Diskon Tiket 20%"
else:
    keterangan = "Diskon Tiket 40%"

# Menampilkan hasil
print(f"Tinggi Anak: {tinggi} cm")
print(f"Umur Anak: {umur} tahun")
print(f"Keterangan: {keterangan}")
