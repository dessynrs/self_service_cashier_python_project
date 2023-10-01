"""
File ini dipisahkan khusus untuk pembuatan database dan tabel pada SQLite3.
Anda harus menjalankan file ini sebelum menjalankan file 'modules.py' dan 'main.py'.
Urutan file yang harus dijalankan :
1. setup_db.py (1x)
2. modules.py (1x)
3. main.py (program utama)

Output dari dijalankannya file ini adalah database 'order_super_cashier.db'.
Di dalamnya ada 2 tabel hasil dari program utama :
1. transaction_super_cashier 
    --digunakan untuk memuat hasil transaksi yang berhasil check out pada program utama
2. customer_super_cashier
    --digunakan untuk memuat detail pengiriman customer delivery

Note : 
Modul setup_db hanya berlangsung satu kali (karena create tabel database hanya satu kali)
Jika sudah pernah ada data, tidak perlu menjalankan modul ini lagi.

"""

# import
import sqlite3

def create_db():
    "Fungsi mendefinisikan database yang digunakan saat check out"

    # masukkan dalam database menggunakan sqlite3
    con = sqlite3.connect("order_super_cashier.db")
    cur = con.cursor()

    # create sql table : tabel transaction
    cur.execute("""CREATE TABLE IF NOT EXISTS transaction_super_cashier(
                line TEXT NOT NULL,
                nama_item TEXT NOT NULL, 
                jumlah_item REAL NOT NULL, 
                harga_per_item REAL NOT NULL,
                total_harga REAL NOT NULL,
                diskon REAL NOT NULL,
                harga_setelah_diskon REAL NOT NULL,
                kode_transaksi TEXT NOT NULL
                )""")

    # create sql table :  tabel customer delivery
    cur.execute("""CREATE TABLE IF NOT EXISTS customer_super_cashier(
                id_customer INTEGER PRIMARY KEY,
                nama TEXT NOT NULL, 
                alamat TEXT NOT NULL, 
                kota TEXT NOT NULL,
                kode_pos TEXT NOT NULL,
                telepon TEXT NOT NULL,
                no_transaksi TEXT NOT NULL
                )""")
    
    return con, cur

# LINE TERAKHIR - CODE DITUTUP



