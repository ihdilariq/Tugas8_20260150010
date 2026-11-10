#Modul Pustaka Logika Sistem Monitoring Presisi IoT
#Kampung Anggur Plumbungan

#1. KONSTANTA (TUPLE)
LOKASI = ("Kampung Anggur Plumbungan", -7.828, 110.378)
AMBANG_KRITIS = (35.0, 40.0)   #(Suhu Max C, Kelembaban Min %)

#2. FUNGSI HITUNG TREN
def hitung_tren(data_slice):
    """Menerima list tuple (suhu, kelembaban) hasil slicing,
    mengembalikan rata-rata suhu dan rata-rata kelembaban."""
    total_suhu = 0
    total_lembab = 0

    for suhu, lembab in data_slice:
        total_suhu += suhu
        total_lembab += lembab

    jumlah = len(data_slice)
    rata_suhu = total_suhu / jumlah
    rata_lembab = total_lembab / jumlah

    return rata_suhu, rata_lembab

#3. FUNGSI EVALUASI IRIGASI
def evaluasi_irigasi(rata_suhu, rata_lembab, tuple_kritis):
    """Menentukan status pompa berdasarkan ambang kritis."""
    suhu_max = tuple_kritis[0]
    lembab_min = tuple_kritis[1]

    if rata_suhu > suhu_max or rata_lembab < lembab_min:
        return "KRITIS: Nyalakan Pompa Irigasi!"
    else:
        return "NORMAL: Pompa Mati."