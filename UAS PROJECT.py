# Dictionary untuk menyimpan harga makanan
menu_harga = {
    'nasi_goreng': 15000,
    'ayam geprek': 12000,
    'mie nyemek': 18000,
    'kwetiaw': 20000,
    'soto': 15000
}

# Inisialisasi variabel total harga
total_harga = 0

# List untuk menyimpan pesanan
pesanan = []

# Meminta input pilihan makanan dari pengguna
while True:
    print("\nMenu Makanan:")
    for item, harga in menu_harga.items():
        print(f"{item.capitalize()}: Rp {harga}")

    pilihan = input("\nMasukkan pilihan makanan (selesai untuk menyelesaikan pesanan): ").lower()

    if pilihan == 'selesai':
        break

    if pilihan in menu_harga:
        pesanan.append(pilihan)
        total_harga += menu_harga[pilihan]
        print(f"{pilihan.capitalize()} ditambahkan ke pesanan.")
    else:
        print("Menu tidak valid. Silakan pilih menu yang valid.")

# Menampilkan struk pembelian
print("\n===== Struk Pembelian =====")
for item in pesanan:
    print(f"{item.capitalize()}: Rp {menu_harga[item]}")

print("============================")
print(f"Total Harga: Rp {total_harga}")
