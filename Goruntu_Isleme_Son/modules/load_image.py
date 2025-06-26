import numpy as np
from tkinter import filedialog
import cv2

def load_image(path):
    img = cv2.imread(path)

    if img is None:
        print("Görsel yüklenemedi.")
        return None

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    h, w = img.shape[:2]
    max_width = 256
    max_height = 256

    if w > max_width or h > max_height:
        print("Görsel çok büyük, otomatik olarak küçültülüyor...")

        if h > w:
            scale = max_height / h
        else:
            scale = max_width / w

        new_width = int(w * scale)
        new_height = int(h * scale)

        resized_img = np.zeros((new_height, new_width, 3), dtype=np.uint8)

        for i in range(new_height):
            for j in range(new_width):
                resized_img[i, j] = img[min(int(i / scale), h - 1), min(int(j / scale), w - 1)]

        img = resized_img

    return img

def load_image_user():
    path = filedialog.askopenfilename()
    if path:
        return load_image(path)
    return None
