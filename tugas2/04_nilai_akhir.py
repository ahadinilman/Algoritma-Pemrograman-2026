# Berkas: latihan/04_nilai_akhir.py

nama = input("Masukkan nama mahasiswa: ")
nilai_tugas = float(input("Masukkan nilai Tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

nilai_akhir = (0.20 * nilai_tugas) + (0.30 * nilai_uts) + (0.50 * nilai_uas)

print(f"\nMahasiswa : {nama}")
print(f"Nilai Akhir : {nilai_akhir:.2f}")