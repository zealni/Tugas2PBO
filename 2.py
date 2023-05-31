class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama Mahasiswa:", self.nama)
        print("NIM Mahasiswa:", self.nim)
        print("Jurusan Mahasiswa:", self.jurusan.nama_jurusan)


class Jurusan:
    def __init__(self, nama_jurusan):
        self.nama_jurusan = nama_jurusan
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.nama_jurusan)
        for mahasiswa in self.daftar_mahasiswa:
            print("- Nama:", mahasiswa.nama)
            print("  NIM:", mahasiswa.nim)
            print()


class Universitas:
    def __init__(self, nama_universitas):
        self.nama_universitas = nama_universitas
        self.daftar_jurusan = []

    def tambah_jurusan(self, jurusan):
        self.daftar_jurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.nama_universitas)
        for jurusan in self.daftar_jurusan:
            print("- Nama Jurusan:", jurusan.nama_jurusan)
            print()


# Membuat objek Universitas
universitas_xyz = Universitas("XYZ University")

# Membuat objek Jurusan
jurusan_ti = Jurusan("Teknik Informatika")

# Menambahkan objek Jurusan ke dalam Universitas
universitas_xyz.tambah_jurusan(jurusan_ti)

# Membuat objek Mahasiswa
mahasiswa_1 = Mahasiswa("Arief Setiawan", "G1A0220555", jurusan_ti)

# Menambahkan objek Mahasiswa ke dalam Jurusan
jurusan_ti.tambah_mahasiswa(mahasiswa_1)

# Menampilkan daftar jurusan di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()

# Menampilkan daftar mahasiswa di Jurusan Teknik Informatika di Universitas XYZ
jurusan_ti.tampilkan_daftar_mahasiswa()
