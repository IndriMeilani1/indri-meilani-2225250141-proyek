# Test Case - Program Analisis Nilai Mahasiswa

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat membaca data nilai mahasiswa, menghitung rata-rata, menentukan nilai minimum dan maksimum, menghitung jumlah mahasiswa yang lulus, serta menangani data yang tidak valid.

## 2. Daftar Test Case

### TC01 - Data Nilai Normal

Input:
- Nilai: 80, 70, 90

Hasil yang Diharapkan:
- Rata-rata: 80.00
- Nilai minimum: 70
- Nilai maksimum: 90
- Semua data berhasil diproses.

Status: PASS.

### TC02 - Nilai Batas Kelulusan

Input:
- Nilai: 60
- Batas kelulusan: 60

Hasil yang Diharapkan:
- Mahasiswa dinyatakan lulus karena nilai sama dengan batas kelulusan.

Status: PASS.

### TC03 - Nilai Melebihi Batas Maksimum

Input:
- NIM: A009
- Nilai: 101

Hasil yang Diharapkan:
- Data ditolak karena nilai melebihi rentang 0 sampai 100.
- Program tetap berjalan.

Status: PASS.

### TC04 - Data Nilai Tidak Valid

Input:
- NIM: A007
- Nilai: abc

Hasil yang Diharapkan:
- Data tidak valid dilewati.
- Program menampilkan pesan kesalahan.
- Data mahasiswa lainnya tetap diproses.

Status: PASS.

### TC05 - File Input Tidak Ditemukan

Input:
- Nama file: data/tidak_ada.txt

Hasil yang Diharapkan:
- Program menampilkan pesan bahwa file tidak ditemukan.
- Program tidak berhenti secara tiba-tiba.

Status: PASS.

### TC06 - File Input Kosong

Input:
- File tersedia, tetapi tidak memiliki data.

Hasil yang Diharapkan:
- Jumlah data valid: 0
- Rata-rata: 0.00
- Program tidak mengalami pembagian dengan nol.
- Program menampilkan pesan bahwa tidak ada data nilai yang valid.

Status: PASS.

### TC07 - Pengujian Menggunakan Data Contoh

Input:
- Data dari file data/contoh_data.txt.

Hasil yang Diharapkan:
- Jumlah data valid: 7
- Rata-rata nilai: 76.00
- Nilai minimum: 55
- Nilai maksimum: 92
- Jumlah mahasiswa lulus: 6
- Jumlah mahasiswa tidak lulus: 1

Status: PASS.

## 3. Catatan Pengujian

Setiap test case dijalankan untuk membandingkan hasil aktual dengan hasil yang diharapkan. Jika hasilnya sesuai, status pengujian diubah menjadi PASS. Jika hasilnya tidak sesuai, status diubah menjadi FAIL dan program perlu diperiksa kembali.

## 4. Catatan Debugging

Pengujian dilakukan untuk menemukan kesalahan pada proses pembacaan data, validasi nilai, perhitungan rata-rata, dan penentuan status kelulusan. Salah satu pengujian menggunakan data tidak valid berupa nilai abc untuk memastikan program dapat melewati data yang salah tanpa menghentikan proses pembacaan data lainnya.

## 5. Retest

Setelah kesalahan ditemukan dan diperbaiki, pengujian dilakukan kembali pada bagian yang mengalami kesalahan. Pengujian juga dilakukan pada beberapa test case lainnya untuk memastikan perbaikan tidak menimbulkan kesalahan baru.