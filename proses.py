def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0

    return sum(nilai) / len(nilai)


def status_lulus(nilai, batas=60):
    return [x for x in nilai if x >= batas]


def ringkasan(data):
    nilai = [item["nilai"] for item in data]

    return {
        "jumlah": len(nilai),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": min(nilai) if nilai else None,
        "maksimum": max(nilai) if nilai else None,
        "lulus": len(status_lulus(nilai))
    }