# Berkas: tugas/kalkulator_koordinat.py

"""
Program: Kalkulator Koordinat 2D
Nama   : [Isi Nama Anda]
NIM    : [Isi NIM Anda]
Kelas  : [Isi Kelas Anda]
Deskripsi: Memproses koordinat dua titik A dan B, menghitung perubahan koordinat (dx, dy),
           jarak Euclidean, dan titik tengah tanpa fungsi buatan, loop, kondisi, atau pustaka eksternal.
"""

# Input koordinat sebagai float
x1 = float(input("Masukkan x1 (Titik A): "))
y1 = float(input("Masukkan y1 (Titik A): "))
x2 = float(input("Masukkan x2 (Titik B): "))
y2 = float(input("Masukkan y2 (Titik B): "))

# Perhitungan delta
dx = x2 - x1
dy = y2 - y1

# Perhitungan jarak Euclidean dan titik tengah
jarak = ((dx ** 2) + (dy ** 2)) ** 0.5
mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2

# Output terformat dengan dua angka desimal
print("\n--- HASIL PERHITUNGAN ---")
print(f"Koordinat Titik A : ({x1:.2f}, {y1:.2f})")
print(f"Koordinat Titik B : ({x2:.2f}, {y2:.2f})")
print(f"dx                : {dx:.2f}")
print(f"dy                : {dy:.2f}")
print(f"Jarak Euclidean   : {jarak:.2f}")
print(f"Titik Tengah      : ({mid_x:.2f}, {mid_y:.2f})")