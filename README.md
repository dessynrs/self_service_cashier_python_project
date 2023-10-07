# ****Self-service Cashier Register****

Program Self-service cashier sederhana yang dibuat dengan menggunakan bahasa pemrograman Python dan terhubung dengan database SQLite3 

Note : code dapat dilihat pada branch master

## **Tujuan Pengerjaan Proyek**

Membuat program sederhana self-service cashier untuk sebuah supermarket, sebagai tugas akhir proyek Python Introduction to Data & Software Engineering - Sekolah Data Engineering Pacmann.

1. Pengaplikasian create function berdasarkan requirements (add, update, delete, check out)
2. Pengaplikasian clean code
3. Pengaplikasian integrasi program dengan database SQLite3
4. Code Sharing dalam github


## **Flow Chart**

Berikut flow chart dari program ini. 

![alt text](https://github.com/dessynrs/self_service_cashier_python_project/blob/master/flow%20chart%20customer_journey.png?raw=true)

Dan berikut database sederhana hasil dari program ini.

![alt text](https://github.com/dessynrs/self_service_cashier_python_project/blob/master/database.png?raw=true)


## **Deskripsi File**

1. File "setup_db.py" berisi fungsi pembuatan database untuk menampung hasil akhir program
2. File "modules.py" berisi fungsi-fungsi untuk pembuatan program dan semua fiturnya
3. File "main.py" sebagai file utama program yang hanya bisa dijalankan jika sudah menjalankan "setup_db.py" dan "modules.py"
4. File "order_super_cashier.db" yang berisi 2 tabel transaksi dan customer sebagai hasil uji coba menjalankan program
5. File tambahan berupa hasil test case sesuai tugas proyek
6. File presentasi dan flow chart


## **Cara Menjalankan Program**

1. Download semua 3 file utama python (*.py) ke dalam satu direktori lokal.
2. Jalankan "setup_db.py" di terminal -- hanya perlu satu kali.
3. Jalankan "modules.py" di terminal -- hanya perlu satu kali.
4. Jalankan "main.py" di terminal setiap akan masuk dalam program Self-service Cashier Register.
5. Urutan setelahnya menyesuaikan kebutuhan (sudah masuk dalam fitur program).


# **Saran pengembangan**

1. Penggunaan database server seperti PostgreSQL atau MySQL supaya lebih padu
2. Penyederhanaan ID transaksi
3. Pembuatan relational database (RDBMS) yang lebih lengkap sebagai pelengkap pencatatan order yang mempermudah owner dalam memperoleh kondisi keseluruhan bisnis
4. Pemberian akses login customer sehingga semua customer dapat tercapture, baik customer langsung maupun customer delivery


