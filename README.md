Sesuai dengan soal yang sudah diberikan, kita diminta untuk membuat 3 kelas obek yaitu mahasiswa,jurusan,dan universitas.
Di dalam kode di atas, terdapat tiga kelas objek yang saling berhubungan: Mahasiswa, Jurusan, dan Universitas.
1. Kelas Mahasiswa:
- Kelas ini memiliki atribut:
- Nama: untuk menyimpan nama mahasiswa (bertipe string)
- NIM: untuk menyimpan nomor induk mahasiswa (bertipe string)
- Jurusan: untuk menyimpan objek Jurusan yang menjadi jurusan mahasiswa
- Kelas ini memiliki metode:
- `__init__(self, nama, nim, jurusan)`: metode inisialisasi yang digunakan untuk menginisialisasi atribut Nama, NIM, dan Jurusan saat objek Mahasiswa dibuat.
- `tampilkan_info(self)`: metode untuk menampilkan informasi Nama, NIM, dan nama Jurusan mahasiswa.
- 
2. Kelas Jurusan:
- Kelas ini memiliki atribut:
- NamaJurusan: untuk menyimpan nama jurusan (bertipe string)
- DaftarMahasiswa: untuk menyimpan daftar objek Mahasiswa yang terdaftar di jurusan
- Kelas ini memiliki metode:
- `__init__(self, nama_jurusan)`: metode inisialisasi yang digunakan untuk menginisialisasi atribut NamaJurusan dan DaftarMahasiswa saat objek Jurusan dibuat.
- `tambah_mahasiswa(self, mahasiswa)`: metode untuk menambahkan objek Mahasiswa ke dalam daftar DaftarMahasiswa.
- `tampilkan_daftar_mahasiswa(self)`: metode untuk menampilkan daftar mahasiswa yang terdaftar dalam Jurusan.
- 
3. Kelas Universitas:
- Kelas ini memiliki atribut:
- NamaUniversitas: untuk menyimpan nama universitas (bertipe string)
- DaftarJurusan: untuk menyimpan daftar objek Jurusan di universitas
- Kelas ini memiliki metode:
- `__init__(self, nama_universitas)`: metode inisialisasi yang digunakan untuk menginisialisasi atribut NamaUniversitas dan DaftarJurusan saat objek Universitas dibuat.
- `tambah_jurusan(self, jurusan)`: metode untuk menambahkan objek Jurusan ke dalam daftar DaftarJurusan.
- `tampilkan_daftar_jurusan(self)`: metode untuk menampilkan daftar jurusan yang ada di Universitas.
-
Kemudian kita membuat main program yang mana sesuai dengan pertanyaan dari soal yaitu:
- Membuat objek Universitas dengan nama "XYZ College" dengan `universitas_xyz = Universitas("XYZ University")`.
- Membuat objek Jurusan dengan nama "Teknik Informatika" dengan `jurusan_ti = Jurusan("Teknik Informatika")`.
- Menambahkan objek Jurusan ke dalam Universitas dengan menggunakan metode `tambah_jurusan()` pada objek universitas_xyz.
- Membuat objek Mahasiswa dengan nama "Arief Setiawan", NIM "G1A0220555" dan memasukkannya ke dalam Jurusan Teknik Informatika dengan menggunakan metode `tambah_mahasiswa()` pada objek jurusan_ti.
- Menampilkan daftar jurusan yang ada di Universitas XYZ dengan menggunakan metode `tampilkan_daftar_jurusan()` pada objek universitas_xyz.
- Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ dengan menggunakan metode `tampilkan_daftar_mahasiswa()` pada
