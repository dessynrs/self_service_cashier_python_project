"""
Bagian main.py ditujukan sebagai program utama yang harus dijalankan untuk masuk dalam SUPER-CASHIER Register.

Caranya :
* Pada terminal, ketikkan 'py modules.py' atau 'python modules.py' untuk mengaktifkan progam modules
* Setelah itu, pada terminal yg sama, ketikkan 'py main.py' atau 'python main.py' untuk mengaktifkan progam utama.
* Customer dapat langsung melakukan proses input / revisi order sesuai fitur-fitur yang tersedia. 

Adapun fitur2nya meliputi : 
    1 - Add to cart (untuk menambahkan produk keranjang belanja)
    2 - Update item : product name (untuk melakukan perbaikan nama produk yg salah)
    3 - Update item : quantity (untuk melakukan perbaikan qty produk yg salah)
    4 - Update item : price (untuk melakukan perbaikan harga produk yg salah)
    5 - Delete item (untuk menghapus produk yang salah)
    6 - Reset transaction (untuk menghapus seluruh transaksi)
    7 - Check order (untuk melakukan cek order sebelum check out)
    8 - Check out (untuk langsung melakukan check out)
    9 - CLOSE (untuk keluar dari program, semua order dalam keranjang akan terhapus)

Reminder :
Sebelum mengakses main.py, Anda wajib sudah menjalankan file 'setup_db.py' dan 'modules.py'
Urutan file yang harus dijalankan :
1. setup_db.py (1x)
2. modules.py (1x)
3. main.py (program utama)

"""

# import modules
from modules import *

# memulai register
start()

# LINE TERAKHIR - CODE DITUTUP