
from PIL import Image # python3 -m pip install Pillow

import os
#Users/marge/Desktop/LAS HORMIGUITAS/IMG PARA USAR
downloadsFolder = "/Users/marge/Desktop/LAS HORMIGUITAS/IMG PARA USAR/nuevas/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png", "JPG"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(downloadsFolder + "compressed_"+filename, optimize=True, quality=60)