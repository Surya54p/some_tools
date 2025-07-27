import cv2
import os

input_folder = "dataset"
output_folder = "dataset_kompres"
os.makedirs(output_folder, exist_ok=True)

scale_percent = 50  # Ubah ini sesuai keperluan (misal 50% dari ukuran asli)
jpeg_quality = 85   # 100 = kualitas maksimum, 85 = udah bagus banget

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        img = cv2.imread(input_path)

        # Resize
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        resized = cv2.resize(img, (width, height))

        # Simpan dengan kualitas JPEG
        cv2.imwrite(output_path, resized, [cv2.IMWRITE_JPEG_QUALITY, jpeg_quality])

        print(f"Sukses kompres {filename}")
