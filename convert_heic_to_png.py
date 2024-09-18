from PIL import Image
from threading import Thread
import os
from sys import argv
import pillow_heif

def convert_file(path):
    new_path = path.replace(".heic", ".png")
    heif_file = pillow_heif.open_heif(path)
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data, 
        "raw", 
        heif_file.mode, 
        heif_file.stride
    )
    image.save(new_path, "PNG")

if len(argv) == 2:
    path = argv[1]
    print(f"Searching: {path}")
    if os.path.isdir(path):
        print("Is directory.")
        threads = []
        for img in os.listdir(path):
            if img.split(".")[-1] == "heic":
                print(f"Converting {img}")
                threads.append(Thread(target=lambda: convert_file(f"{path}\\{img}")))
                threads[-1].start()
    elif os.path.isfile(path):
        print(f"Converting {path}")
        convert_file(path)
    else:
        print(f"Err: {path} is not a dir or file.")
else:
    print("Expected python convert_heic_to_png.py <PATH>")
