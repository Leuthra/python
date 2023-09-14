print("""
 _  __     _ _          _       _             
| |/ /    | | |        | |     | |            
| ' / __ _| | | ___   _| | __ _| |_ ___  _ __ 
|  < / _` | | |/ / | | | |/ _` | __/ _ \| '__|
| . \ (_| | |   <| |_| | | (_| | || (_) | |   
|_|\_\__,_|_|_|\_\\__,_|_|\__,_|\__\___/|_|  w 
            Matematika tidak asik
"jangan suka menghitung, apalagi menghitung perasaan"
""")

# Function Calc
def tambahin(x, y):
    return x + y

def kurang(x, y):
    return x - y

def dikali(x, y):
    return x * y

def dibagi(x, y):
    if y == 0:
        return "Tidak dapat dibagi dengan nol"
    return x / y

while True:
    print("Pilih Operasi.")
    print("1. Jumlah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

    choice = input("Masukkan pilihan(1/2/3/4/5): ")

    if choice == '5':
        break
    # keluar dari program

    if choice not in ('1', '2', '3', '4'):
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 5 (untuk keluar).")
        continue

    num1 = int(input("Masukkan bilangan pertama: "))
    num2 = int(input("Masukkan bilangan kedua: "))

    if choice == '1':
        print(num1, "+", num2, "=", tambahin(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", kurang(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", dikali(num1, num2))

    elif choice == '4':
        result = dibagi(num1, num2)
        # isinstance digunakan untuk mengecek tipe data object
        if isinstance(result, str):
            print(result)
        else:
            print(num1, "/", num2, "=", result)
