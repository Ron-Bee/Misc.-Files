  GNU nano 5.4                          image_converter.py *
#!/usr/bin/env python3

from PIL import Image
import os
import zipfile
input_folder = "images.zip"
output_folder = "/opt/icons"
input_zip = "images.zip"
os.makedirs(output_folder, exist_ok=True)

with zipfile.ZipFile(input_zip, 'r') as zip_ref:
        zip_ref.extractall(output_folder)

for filename in os.listdir(input_folder):
        with Image.open(os.path.join(input_folder, filename)) as img:
                img = img.rotate(-90, expand=True)
                img = img.resize((128,128))
                output_filename = os.path.splitext(filename)[0] + ".jpg"
                img.save(os.path.join(output_folder, output_filename), "JPEG")

for filename in os.listdir("/tmp"):
    file_path = os.path.join("/tmp", filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
