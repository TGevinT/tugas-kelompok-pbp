# MedStem
## Tugas Kelompok PBP Gasal 2022/2023

# How to Run
1. Create venv
```
python -m venv env
```

2. Activate venv
```
Windows
env/Scripts/activate
Linux
source env/bin/activate
```

3. install dependencies
```
pip install -r requirements.txt
```

4. Run
```
python manage.py runserver
```

# Nama-nama anggota kelompok
1. Naila Azizah - 2106705814
2. Amelia Putri Chaerani - 2106751985
3. Teuku Gevin Taufan
4. Rafif Naufal Rahmadika - 2106636275
5. Nicholas Sidharta - 2106752294

# Tautan aplikasi Heroku
https://medstem.herokuapp.com/

# Cerita aplikasi yang diajukan serta manfaatnya
Aplikasi yang akan kami buat adalah sebuah aplikasi untuk memudahkan pelayanan rumah sakit. Aplikasi ini digunakan oleh tenaga medis dan kesehatan dalam rumah sakit guna memudahkan tenaga medis untuk menyusun jadwal pasien, mengalokasikan ruangan yang digunakan untuk pasien, tracking aktivitas lab, tracking request obat, dan menghitung pendapatan harian dari sebuah rumah sakit. Selain itu, dengan menggunakan aplikasi yang dibuat oleh kami dapat mempermudah komunikasi akses antar komponen rumah sakit sehingga tidak terjadi bentrok satu dengan yang lainnya.

# Daftar modul yang akan diimplementasikan
Dari manfaat yang disebutkan diatas, maka kelompok kami membuat lima fitur dalam menunjang aplikasi ini, sebagai berikut:
1. Implementasi Register, login, logout
Fitur ini mengelompokkan halaman sesuai dengan peran user yang login karena setiap peran akan mendapatkani fitur yang berbeda
2. Childcare : mengatur antrian dokter anak
Fitur ini akan dapat diakses oleh tenaga medis khusus anak dan meliputi views sebagai berikut:
    - add_queue: untuk menambahkan seorang pasien ke dalam antrian
    - show_queue: untuk menunjukkan antrian pasien anak yang ada
    - patient_status: untuk menunjukkan status dari pasien anak, seperti masih menunggu, mengeluarkan diri dari antrian, sedang dalam pemeriksaan, sedang menunggu obat, atau sudah selesai berobat.
    - patient_payment_status: untuk menunjukkan apakah pasien sudah membayar biaya berobat atau belum
3. Rawat Jalan : mengatur antrian dokter umum
Fitur ini akan dapat diakses oleh tenaga medis dokter umum dan perawat dan meliputi views sebagai berikut:
    - add_queue: untuk menambahkan seorang pasien ke dalam antrian
    - show_queue: untuk menunjukkan antrian pasien yang ada
    - patient_status: untuk menunjukkan status dari pasien, seperti masih menunggu, mengeluarkan diri dari antrian, sedang dalam pemeriksaan, sedang menunggu obat, atau sudah selesai berobat.
    - patient_payment_status: untuk menunjukkan apakah pasien sudah membayar biaya berobat atau belum
4. Vaksin : track aktivitas vaksin
    - get_vaksin_data: mendapatkan data mengenai jenis-jenis vaksin
    - get_stock: mendapatkan data stock 1 jenis vaksin
    - edit_dose: mengubah dosis vaksin yang diberikan
    - get_vaksin_history: mendapatkan data vaksin yang sudah didapat (sebagai pasien)
    - add_vaksin: menambah jenis vaksin yang akan digunakan pada pasien
5. Apotek : track request obat
    - get_patient_data: untuk mendapatkan data dari pasien
    - add_resep: untuk mengirimkan rekomendasi resep obat 
    - get_resep: untuk mendapatkan data obat yang direkomendasikan oleh dokter kepada pasien
    - resep_status: untuk menunjukkan status dari pasien, seperti apakah sedang menunggu obat atau sudah mengambil obat
    - patient_payment_status: untuk menunjukkan apakah pasien sudah membayar obat atau belum
6. Kasir : track transaksi yang dilakukan perhari
    - get_payment_data: untuk mendapatkan data transaksi yang sudah terjadi hari itu
    - get_payment: untuk mengambil uang yang ada di mesin kasir

# Role atau peran pengguna beserta deskripsinya (karena bisa saja lebih dari satu jenis pengguna yang mengakses aplikasi)
Pengguna yang dituju dalam aplikasi ini adalah healthcare staff dalam rumah sakit. Dalam sebuah rumah sakit terdapat dokter, perawat, apoteker, ahli teknologi lab, radiografer, kasir. Masing - masing memiliki tanggung jawab sesuai dengan pekerjaannya. Peran pengguna dan deskripsinya:
1. Dokter → mengatur antrian dengan pasien, bisa chat dengan tenaga medis lain, mengatur dosis vaksin, menambahkan vaksin, dan mendapatkan data tentang vaksin
2. Perawat → membuat shift kerja sesuai dengan dokter pendamping, chat dengan tenaga medis lain (umumnya apoteker)
3. Apoteker →tracking request obat, tracking obat yang habis dan akan dibeli lagi, tracking obat yang keluar dan masuk, tracking stock vaksin, dan mendapatkan data tentang vaksin.
4. Ahli Farmasi → meracik obat yang berjenis racikan berdasarkan request
5. Ahli teknologi lab → tracking aktivitas lab (alat - alat yang digunakan di lab), tracking hasil lab
6. Radiografer →tracking aktivitas lab (alat - alat yang digunakan di lab), tracking hasil lab
7. Kasir → tracking pemasukan harian yang didapatkan di rumah sakit dari konsultasi dokter, pembelian obat di apotek, atau melakukan test lab.
8. Pasien → melihat riwayat vaksinasi
