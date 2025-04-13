import cv2
import os

# PROSEDUR:

# 1. Buat folder untuk setiap objek yang ingin dicrop, misalnya "buku".
#    Letakkan semua gambar mentah dari objek tersebut ke dalam folder "buku".

# 2. Ulangi langkah di atas untuk objek lain.
#    Pastikan semua folder (contoh: buku, pensil, penghapus) berada dalam satu folder utama sebagai dataset.

# 3. Masukkan path dari folder utama (yang berisi semua folder objek) ke dalam variabel sumber pada kode Python.
#    Contoh:
#    sumber_dataset = "path/ke/folder/dataset"


# Pilih folder sumber (misal "Dataset1")
folder_sumber = r"D:\muba\Documents\Matlab project folder\Pelatihan AI Gasim\surya\deteksi_font\dataset"  # Ganti dengan folder utama dataset

# Looping semua kategori dalam folder sumber
for kategori in os.listdir(folder_sumber):
    path_kategori = os.path.join(folder_sumber, kategori)

    # Cek apakah ini folder
    if os.path.isdir(path_kategori):
        # Buat folder tujuan dengan nama yang sama + "_crop"
        folder_tujuan = path_kategori + "_crop"
        if not os.path.exists(folder_tujuan):
            os.makedirs(folder_tujuan)

        # Ambil semua gambar dalam folder kategori
        gambar_list = [f for f in os.listdir(path_kategori) if f.endswith((".jpg", ".png", ".jpeg"))]
        gambar_list.sort()  # Urutkan gambar sesuai nama

        for file_name in gambar_list:
            # Baca gambar
            path_gambar = os.path.join(path_kategori, file_name)
            img = cv2.imread(path_gambar)

            if img is None:
                print(f"❌ Gagal membaca {file_name} di {kategori}")
                continue

            # **Resize hanya untuk tampilan, agar tidak terlalu besar**
            max_width = 600  # Atur lebar maksimal agar tidak terlalu besar
            scale = max_width / img.shape[1] if img.shape[1] > max_width else 1
            new_size = (int(img.shape[1] * scale), int(img.shape[0] * scale))
            img_resized = cv2.resize(img, new_size) if scale < 1 else img

            # Pilih area yang ingin dikrop (manual)
            roi = cv2.selectROI(f"Pilih area untuk {file_name}, lalu tekan ENTER", img_resized, fromCenter=False, showCrosshair=True)

            # Jika area valid, lakukan crop dan simpan
            if roi != (0, 0, 0, 0):  # Hindari penyimpanan jika user cancel
                # Konversi koordinat ROI ke ukuran asli
                x, y, w, h = [int(coord / scale) for coord in roi]
                cropped_img = img[y:y+h, x:x+w]

                # Simpan hasil crop ke folder tujuan dengan nama file yang sama
                path_simpan = os.path.join(folder_tujuan, file_name)
                cv2.imwrite(path_simpan, cropped_img)

                print(f"✅ {file_name} berhasil disimpan di {folder_tujuan}")

            # Tutup jendela OpenCV
            cv2.destroyAllWindows()

print("🎉 Semua gambar selesai diproses!")
