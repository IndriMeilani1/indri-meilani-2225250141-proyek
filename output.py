def tampilkan_rekap(data, hasil):
    print("\n===== REKAP ANALISIS NILAI MAHASISWA =====")
    print(f"Jumlah data valid : {hasil['jumlah']}")
    print(f"Rata-rata nilai   : {hasil['rata_rata']:.2f}")

    if hasil["jumlah"] > 0:
        print(f"Nilai minimum     : {hasil['minimum']:.2f}")
        print(f"Nilai maksimum    : {hasil['maksimum']:.2f}")
        print(f"Jumlah lulus      : {hasil['lulus']}")
        print(f"Jumlah tidak lulus: {hasil['jumlah'] - hasil['lulus']}")

        print("\nDetail Nilai:")
        for item in data:
            status = "Lulus" if item["nilai"] >= 60 else "Tidak Lulus"
            print(
                f"{item['nim']} | "
                f"{item['nilai']:.2f} | {status}"
            )
    else:
        print("Tidak ada data nilai yang valid.")


def simpan_rekap(nama_file, hasil):
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("REKAP ANALISIS NILAI MAHASISWA\n")
        file.write("==============================\n")
        file.write(f"Jumlah data valid: {hasil['jumlah']}\n")
        file.write(f"Rata-rata: {hasil['rata_rata']:.2f}\n")

        if hasil["jumlah"] > 0:
            file.write(f"Nilai minimum: {hasil['minimum']:.2f}\n")
            file.write(f"Nilai maksimum: {hasil['maksimum']:.2f}\n")
            file.write(f"Jumlah lulus: {hasil['lulus']}\n")
            file.write(
                f"Jumlah tidak lulus: "
                f"{hasil['jumlah'] - hasil['lulus']}\n"
            )

    print(f"\nRekap berhasil disimpan ke {nama_file}")