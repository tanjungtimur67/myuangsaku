#!/usr/bin/env python3
"""Main entrypoint embedding the mymyuanguang application."""
import json
import os

saldo = 0
pemasukan_list = []
pengeluaran_list = []
FILE_DATA = "data_uangsaku.json"

def muat_data():
    global saldo, pemasukan_list, pengeluaran_list
    if os.path.exists(FILE_DATA):
        try:
            with open(FILE_DATA, 'r') as file:
                data = json.load(file)
                saldo = data.get('saldo', 0)
                pemasukan_list = data.get('pemasukan', [])
                pengeluaran_list = data.get('pengeluaran', [])
        except:
            print("Gagal memuat data")

def simpan_data():
    global saldo, pemasukan_list, pengeluaran_list
    data = {
        'saldo': saldo,
        'pemasukan': pemasukan_list,
        'pengeluaran': pengeluaran_list
    }
    with open(FILE_DATA, 'w') as file:
        json.dump(data, file, indent=2)

def tambah_pemasukan():
    global saldo, pemasukan_list
    try:
        jumlah = float(input("Masukkan jumlah pemasukan (Rp): "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            return
        saldo += jumlah
        pemasukan_list.append(jumlah)
        print(f"✓ Pemasukan berhasil ditambahkan!")
        print(f"  Jumlah: Rp {jumlah:,.0f}")
        print(f"  Saldo sekarang: Rp {saldo:,.0f}")
        simpan_data()
    except ValueError:
        print("Input tidak valid! Gunakan angka.")

def tambah_pengeluaran():
    global saldo, pengeluaran_list
    try:
        jumlah = float(input("Masukkan jumlah pengeluaran (Rp): "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            return
        if jumlah > saldo:
            print(f"⚠ PERINGATAN: Saldo tidak cukup!")
            print(f"  Saldo: Rp {saldo:,.0f}")
            print(f"  Pengeluaran: Rp {jumlah:,.0f}")
            print(f"  Kurang: Rp {jumlah - saldo:,.0f}")
            return
        saldo -= jumlah
        pengeluaran_list.append(jumlah)
        print(f"✓ Pengeluaran berhasil dicatat!")
        print(f"  Jumlah: Rp {jumlah:,.0f}")
        print(f"  Saldo sekarang: Rp {saldo:,.0f}")
        simpan_data()
    except ValueError:
        print("Input tidak valid! Gunakan angka.")

def lihat_saldo():
    print(f"\n{'='*40}")
    print(f"Saldo Anda: Rp {saldo:,.0f}")
    print(f"{'='*40}\n")

def lihat_laporan():
    total_pemasukan = sum(pemasukan_list)
    total_pengeluaran = sum(pengeluaran_list)
    
    print(f"\n{'='*40}")
    print(f"LAPORAN KEUANGAN UANG SAKU")
    print(f"{'='*40}")
    print(f"Total Pemasukan   : Rp {total_pemasukan:,.0f}")
    print(f"Total Pengeluaran : Rp {total_pengeluaran:,.0f}")
    print(f"Saldo Akhir       : Rp {saldo:,.0f}")
    print(f"{'='*40}\n")
    
    if pemasukan_list:
        print("Detail Pemasukan:")
        for i, item in enumerate(pemasukan_list, 1):
            print(f"  {i}. Rp {item:,.0f}")
    
    if pengeluaran_list:
        print("\nDetail Pengeluaran:")
        for i, item in enumerate(pengeluaran_list, 1):
            print(f"  {i}. Rp {item:,.0f}")
    print()

def menu():
    print("\n=== APLIKASI PENGELOLA UANG SAKU ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Lihat laporan")
    print("5. Keluar")
    print("="*35)

def main():
    muat_data()

    while True:
        menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_pemasukan()
        elif pilihan == "2":
            tambah_pengeluaran()
        elif pilihan == "3":
            lihat_saldo()
        elif pilihan == "4":
            lihat_laporan()
        elif pilihan == "5":
            print("Terima kasih! Data telah disimpan.")
            simpan_data()
            break
        else:
            print("Pilihan tidak valid! Pilih 1-5.")

if __name__ == "__main__":
    main()
