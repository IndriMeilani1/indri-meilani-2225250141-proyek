# Program Analisis Nilai Mahasiswa

## Deskripsi
Program Analisis Nilai Mahasiswa merupakan program sederhana menggunakan Python yang dibuat untuk membantu mengolah dan menganalisis data nilai mahasiswa. Program ini dapat membaca data dari file teks, kemudian menghitung rata-rata nilai, nilai tertinggi, nilai terendah, serta jumlah mahasiswa yang lulus dan tidak lulus. Pengguna sasaran program ini adalah mahasiswa, dosen, atau siapa saja yang membutuhkan cara sederhana untuk mengolah data nilai secara otomatis.

## Fitur
- Membaca data nilai mahasiswa dari file teks.
- Memvalidasi data agar nilai yang diproses berada pada rentang 0 sampai 100.
- Menghitung jumlah data mahasiswa yang valid.
- Menghitung rata-rata, nilai minimum, dan nilai maksimum.
- Menentukan status kelulusan berdasarkan batas nilai 60.
- Menampilkan hasil analisis ke terminal.
- Menyimpan hasil rekap ke dalam file teks.
- Menangani data tidak valid dan file yang tidak ditemukan.
  
## Persyaratan
- Python 3.x
- Visual Studio Code atau aplikasi editor kode lainnya.
  
## Cara Menjalankan
python3 main.py

## Struktur Folder
- main.py: File utama untuk menjalankan seluruh program.
- src/: Folder yang berisi modul program.
- __init__.py: Menandai folder src sebagai paket Python.
- input_data.py: Berisi fungsi untuk membaca dan memvalidasi data nilai mahasiswa.
- proses.py: Berisi fungsi untuk menghitung rata-rata, nilai minimum, maksimum, dan jumlah mahasiswa yang lulus.
- output.py: Berisi fungsi untuk menampilkan dan menyimpan hasil analisis.
- data/: Folder untuk menyimpan file data.
- contoh_data.txt: Berisi data nilai mahasiswa yang digunakan sebagai input program.
- hasil_rekap.txt: File hasil analisis yang dibuat setelah program dijalankan.
- tests/: Folder untuk menyimpan dokumentasi pengujian.
- test_case.md: Berisi daftar pengujian program dan hasil yang diharapkan.
- docs/: Folder untuk menyimpan dokumentasi proyek.
- screenshot/: Folder untuk menyimpan tangkapan layar hasil program.

## Test Case
Pengujian dilakukan menggunakan beberapa kondisi input untuk memastikan program berjalan dengan benar. Pada TC01, program diuji menggunakan nilai normal yaitu 80, 70, dan 90 dengan hasil yang diharapkan berupa rata-rata 80, nilai minimum 70, dan maksimum 90. Pada TC02, program diuji menggunakan nilai 60 dengan batas kelulusan 60, sehingga mahasiswa diharapkan dinyatakan lulus. Pada TC03, program diuji menggunakan nilai 101 untuk memastikan data di luar rentang 0 sampai 100 ditolak. Pada TC04, program diuji menggunakan data tidak valid berupa nilai abc untuk memastikan program dapat melewati data tersebut tanpa menghentikan proses. Pada TC05, program diuji ketika file input tidak ditemukan dan diharapkan menampilkan pesan kesalahan. Pada TC06, program diuji menggunakan file kosong dengan hasil jumlah data 0 dan rata-rata 0.00 tanpa mengalami pembagian dengan nol. Terakhir, pada TC07, program diuji menggunakan data dari file contoh_data.txt dengan hasil yang diharapkan berupa 7 data valid, rata-rata 76.00, nilai minimum 55, nilai maksimum 92, 6 mahasiswa lulus, dan 1 mahasiswa tidak lulus. Hasil aktual dan status setiap pengujian diisi setelah program benar-benar dijalankan. Jika hasil aktual sesuai dengan hasil yang diharapkan, status pengujian dinyatakan PASS. Jika belum sesuai, statusnya FAIL dan perlu dilakukan perbaikan.

## Known Issues
Beberapa hal yang masih perlu diperhatikan adalah program hanya menerima format data NIM dan nilai yang dipisahkan dengan tanda koma. Data dengan format yang berbeda atau nilai di luar rentang 0 sampai 100 akan dilewati. Selain itu, apabila file input tidak ditemukan, program akan menampilkan pesan kesalahan dan menghasilkan rekap kosong. Program ini masih berupa aplikasi sederhana berbasis terminal dan belum memiliki tampilan antarmuka grafis.

## Anggota dan Kontribusi
Proyek ini dikerjakan secara individu.

## Referensi/Bantuan
- Materi perkuliahan Algoritma dan Pemrograman, khususnya materi implementasi, pengujian, dan dokumentasi proyek.
- ChatGPT (OpenAI), digunakan sebagai bantuan dalam memahami materi, menyusun kode program, memperbaiki kesalahan, dan menyusun dokumentasi proyek.
