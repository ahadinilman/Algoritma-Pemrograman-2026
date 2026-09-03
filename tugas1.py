import math

def hitung_lingkaran():
    try:
        r = float(input("Masukkan jari-jari lingkaran (r): "))
        if r <= 0:
            print("Jari-jari harus lebih besar dari 0!")
            return
        
        luas = math.pi * r ** 2
        keliling = 2 * math.pi * r
        
        print(f"Luas Lingkaran    : {luas:.2f}")
        print(f"Keliling Lingkaran: {keliling:.2f}")
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")

if __name__ == "__main__":
    hitung_lingkaran()