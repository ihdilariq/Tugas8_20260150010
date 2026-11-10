#Mengimpor modul buatan sendiri
import modul_sensor

#1. STRUKTUR DATA UTAMA
log_kebun = []   #berisi tuple (suhu, kelembaban)

#2. FUNGSI VALIDASI INPUT
def input_sensor():
    """Meminta suhu & kelembaban sampai valid (angka, rentang 0-100).
    Mengembalikan tuple (suhu, kelembaban)."""
    while True:
        try:
            suhu = float(input("Masukkan Suhu Udara (C)      : "))
            lembab = float(input("Masukkan Kelembaban Tanah (%) : "))

            if 0 <= suhu <= 100 and 0 <= lembab <= 100:
                return (suhu, lembab)
            else:
                print(">> Error: suhu dan kelembaban harus di rentang 0-100!\n")
        except ValueError:
            print(">> Error: input harus berupa angka, bukan huruf!\n")

#3. PROGRAM UTAMA
print("==============================================")
print("   SISTEM MONITORING PRESISI IoT KEBUN ANGGUR  ")
print(f"   Lokasi: {modul_sensor.LOKASI[0]}")
print(f"   Koordinat: {modul_sensor.LOKASI[1]}, {modul_sensor.LOKASI[2]}")
print("==============================================")

while True:
    print("\n---------------- MENU UTAMA ----------------")
    print("[1] Rekam Data")
    print("[2] Analisis Tren (3 Terakhir)")
    print("[3] Keluar")
    pilihan = input("Pilih menu (1-3): ")

    #MENU 1 : REKAM DATA
    if pilihan == "1":
        print("\n>> REKAM DATA SENSOR")
        data_baru = input_sensor()
        log_kebun.append(data_baru)
        print(f">> Data tersimpan! (Total data: {len(log_kebun)})")

    #MENU 2 : ANALISIS TREN
    elif pilihan == "2":
        if len(log_kebun) == 0:
            print(">> Belum ada data. Silakan rekam data dulu (menu 1).")
        else:
            #Slicing maksimal 3 data terakhir
            tiga_terakhir = log_kebun[-3:]

            print("\n==================================================")
            print("         ANALISIS TREN (3 DATA TERAKHIR)")
            print("==================================================")

            #List iteration for
            nomor = 1
            for data in tiga_terakhir:
                print(f"Data {nomor} -> Suhu: {data[0]:.1f} C | Kelembaban: {data[1]:.1f} %")
                nomor += 1

            #Pemanggilan fungsi modul
            rata_suhu, rata_lembab = modul_sensor.hitung_tren(tiga_terakhir)
            status = modul_sensor.evaluasi_irigasi(rata_suhu, rata_lembab,
                                                   modul_sensor.AMBANG_KRITIS)

            print("--------------------------------------------------")
            print(f"Rata-rata Suhu       : {rata_suhu:.2f} C")
            print(f"Rata-rata Kelembaban : {rata_lembab:.2f} %")
            print(f"Status Irigasi       : {status}")
            print("==================================================")

    #MENU 3 : KELUAR
    elif pilihan == "3":
        print("\nTerima kasih. Program selesai.")
        break

    else:
        print(">> Pilihan tidak valid, masukkan 1, 2, atau 3!")