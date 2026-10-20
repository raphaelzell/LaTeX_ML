'''
This script runs the pix2tex model (https://github.com/lukas-blecher/LaTeX-OCR)
over a given folder of images with latex code
'''

import os
import json

from PIL import Image
from pix2tex.cli import LatexOCR

model = LatexOCR()
mapping_list = []
predictions = {}

for file in os.listdir('example_data'):
    if file.endswith('.png'):
        filename = 'example_data/' + file
        img = Image.open(filename)
        predictions[filename] = model(img)

with open('example_data/predictions.json', "w", encoding="utf-8") as f:
    json.dump(predictions, f, ensure_ascii=False, indent=2)

print(f"{len(predictions)} Vorhersagen gespeichert in {'example_data/predictions.json'}")
