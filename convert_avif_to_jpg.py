import os
import sys
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def convert_folder(folder_path):
    # Vytvoríme podpriečinok "jpg" (ak neexistuje)
    output_folder = os.path.join(folder_path, "jpg")
    os.makedirs(output_folder, exist_ok=True)

    # Prejdeme všetky súbory v priečinku
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.avif'):
            avif_path = os.path.join(folder_path, filename)
            jpg_filename = os.path.splitext(filename)[0] + '.jpg'
            jpg_path = os.path.join(output_folder, jpg_filename)
            try:
                # Otvoríme AVIF, skonvertujeme na RGB a uložíme ako JPEG
                with Image.open(avif_path) as img:
                    rgb_img = img.convert('RGB')
                    rgb_img.save(jpg_path, 'JPEG', quality=95)
                print(f"Prevedené: {filename} → jpg/{jpg_filename}")
            except Exception as e:
                print(f"Chyba pri spracovaní {filename}: {e}")

if __name__ == "__main__":
    # Skryjeme hlavné okno Tkinteru
    root = tk.Tk()
    root.withdraw()

    # Otvoríme dialóg na výber priečinka
    folder = filedialog.askdirectory(title="Vyber priečinok s .avif súbormi")
    if not folder:
        print("Žiadny priečinok nebol vybraný, končím.")
        sys.exit(1)

    convert_folder(folder)
    print("Konverzia hotová!")
