def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                # Lewati baris kosong
                if not baris:
                    continue

                try:
                    bagian = baris.split(",")

                    if len(bagian) != 2:
                        raise ValueError

                    nim = bagian[0].strip()
                    nilai = float(bagian[1].strip())

                    # Validasi NIM dan rentang nilai
                    if not nim or not 0 <= nilai <= 100:
                        print(f"Baris {nomor} tidak valid: {baris}")
                        continue

                    data.append({
                        "nim": nim,
                        "nilai": nilai
                    })

                except ValueError:
                    print(f"Baris {nomor} tidak valid: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return data