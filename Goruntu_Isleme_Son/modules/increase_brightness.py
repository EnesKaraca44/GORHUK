import numpy as np

def increase_brightness(img, value=30):
    """
    Görüntünün parlaklığını artırır.
    Bütün piksel değerlerine 'value' kadar ekler.
    """
    if img is None:
        print("HATA: Parlaklık artırma işlemi için geçerli bir görüntü bulunamadı.")
        return None

    bright_img = img.astype(np.int32) + value
    bright_img = np.clip(bright_img, 0, 255).astype(np.uint8)

    return bright_img
