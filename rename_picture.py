import os
import shutil
input_folder = "dataset_kompres"
output_folder = "dataset_rename"
prefix = "gambar"

os.makedirs(output_folder, exist_ok=True)

i = 1
for file in os.listdir(input_folder):
    if file.lower(). endswith((".jpg",".jpeg",".png")):
        ext = os.path.splitext(file)[1]
        new_name = f"{prefix}_{i}{ext}"

        src = os.path.join(input_folder,file)
        dst = os.path.join(output_folder, new_name)

        shutil.copy2(src, dst)
        print(f"{file} -> {new_name}, done")
        i += 1 

print(f"Semua aktivitas selesai")