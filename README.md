# PROJECT UAS

# Profil

| Variable | Isi |
| -------- | --- |
|**Nama**  | Annisa Saidah Mubarokah |
|**NIM**   | 312310631 |
|**Kelas** | TI.23.A6 |
|**Mata Kuliah** | Bahasa Pemrograman |

# UAS

Buatlah program kasir di sebuah kantin, dengan kondisi berikut:

• List opsi pilihan makanan/minuman dan aksi, bisa menggunakanformat dictionary

• Program harus meminta input pilihan makanan dari pengguna.

• Program harus menghitung total harga makanan yang dipesan.

• Program harus menampilkan struk pembelian.

1. List opsi pilihan makanan/minuman dan aksi, bisa menggunakan format dictionary menu

![Capture 1](https://github.com/annisasaidah06/UAS/assets/148035766/f2b774ba-6fbf-4616-afd7-dfd1607829f3)

Penjelasan
Menu Awal: mencakup beberapa item makanan/minuman beserta harganya. Didefinisikan dalam dictionary menu.

Fungsi tampilkan_menu(): digunakan untuk menampilkan menu makanan/minuman beserta harganya ke layar.

Fungsi hitung_total(): menghitung total harga dari pesanan yang diberikan sebagai argumen.

Fungsi tampilkan_struk(): menampilkan struk pembelian berdasarkan pesanan yang telah dibuat dan total harga.

2. Program harus meminta input pilihan makanan dari pengguna
![Capture 2](https://github.com/annisasaidah06/UAS/assets/148035766/4679b0da-691f-4c86-8ce6-d500f704a19b)

Penjelasan
Fungsi tampilkan_menu() dipanggil di awal untuk menampilkan menu makanan/minuman beserta harganya ke layar.

Sebuah loop while digunakan untuk terus meminta pengguna untuk memilih item dari menu sampai pengguna ingin mengakhiri pesanan dengan mengetikkan 'selesai'. Setiap kali dalam loop, pengguna diminta untuk memasukkan pilihan mereka.
Input pengguna diperiksa:

Jika input adalah 'selesai', loop dihentikan dengan mengubah variabel lanjut menjadi False.

Jika input ada dalam menu, item tersebut ditambahkan ke dalam pesanan.

Jika input tidak ada dalam menu, pesan kesalahan ditampilkan.

3. Program harus menghitung total harga makanan yang dipesan, dan Program harus menampilkan struk pembelian

![Capture 3](https://github.com/annisasaidah06/UAS/assets/148035766/23b26897-999a-45c3-afc2-30a2b9a79a3e)


Penjelasan
Setelah pengguna selesai dengan pesanan, total harga dari pesanan dihitung menggunakan fungsi hitung_total(), dengan menggunakan pesanan sebagai argumen.

Fungsi tampilkan_struk() dipanggil untuk menampilkan struk pembelian berdasarkan pesanan yang telah dibuat dan total harga yang dihitung.

tampilan output:

![ss1](https://github.com/annisasaidah06/UAS/assets/148035766/5be64f6b-63d5-4eb2-b07c-9f0a6750eca7)





