import numpy as np

def rotate_cw(img):
    """
    Görüntüyü saat yönünde 90 derece döndürür.
    """
    if img is None:
        print("HATA: Döndürme işlemi için geçerli bir görüntü bulunamadı.")
        return None

    rotated = np.transpose(img, (1, 0, 2))
    rotated = np.flip(rotated, axis=0)
    return rotated

def rotate_ccw(img):
    """
    Görüntüyü saat yönünün tersine 90 derece döndürür.
    """
    if img is None:
        print("HATA: Döndürme işlemi için geçerli bir görüntü bulunamadı.")
        return None

    rotated = np.transpose(img, (1, 0, 2))
    rotated = np.flip(rotated, axis=1)
    return rotated