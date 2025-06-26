import numpy as np

def binary_conversion(img, threshold=127):
    """
    Gri tonlamalı bir görüntüyü binary (siyah-beyaz) formata çevirir.
    """
    if img is None:
        print("HATA: Binary dönüşüm için geçerli bir görüntü bulunamadı.")
        return None

    if len(img.shape) != 2:
        print("HATA: Binary dönüşüm için giriş görüntüsü gri tonlamalı olmalıdır.")
        return None

    binary = np.where(img > threshold, 255, 0).astype(np.uint8)

    return binary
