romi_tinggi = 170
romi_berat = 55

nanang_tinggi = 165
nanang_berat = 45

lebih_tinggi = romi_tinggi > nanang_tinggi
lebih_berat = romi_berat > nanang_berat

print(f"saya {'lebih tinggi dari' if lebih_tinggi else 'lebih pendek dari atau sama dengan'} tinggi badan nanang.")
print(f"saya {'lebih berat dari' if lebih_berat else 'lebih ringan dari atau sama dengan'} berat badan nanang.")
