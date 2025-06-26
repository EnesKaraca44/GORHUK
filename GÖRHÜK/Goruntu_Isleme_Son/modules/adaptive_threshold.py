import numpy as np
from modules.gray_conversion import gray_conversion

def adaptive_threshold(img, block_size=11, C=2):
    """
    Adaptif threshold uygular (komşuluk ortalamasına göre eşikleme).
    """
    if img is None:
        print("HATA: Adaptif eşikleme için geçerli bir görüntü bulunamadı.")
        return None

    img = gray_conversion(img)

    pad = block_size // 2
    padded_img = np.pad(img, pad, mode='reflect')

    output = np.zeros_like(img)

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            region = padded_img[y:y+block_size, x:x+block_size]
            threshold = np.mean(region) - C
            output[y, x] = 255 if img[y, x] > threshold else 0

    return output
