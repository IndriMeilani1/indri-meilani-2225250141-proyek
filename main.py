from src.input_data import baca_data
from src.proses import ringkasan
from src.output import tampilkan_rekap, simpan_rekap


def main():
    input_file = "data/contoh_data.txt"
    output_file = "data/hasil_rekap.txt"

    # Tahap 1: Membaca data
    data = baca_data(input_file)

    # Tahap 2: Mengolah data
    hasil = ringkasan(data)

    # Tahap 3: Menampilkan hasil
    tampilkan_rekap(data, hasil)

    # Tahap 4: Menyimpan hasil
    try:
        simpan_rekap(output_file, hasil)
    except OSError as error:
        print(f"Gagal menyimpan rekap: {error}")


if __name__ == "__main__":
    main()