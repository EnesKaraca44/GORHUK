import numpy as np

def histogram_equalization(img):
    """
    Gri tonlamalı bir görüntünün histogramını eşitler.
    """
    if img is None:
        print("HATA: Histogram eşitleme işlemi için geçerli bir görüntü bulunamadı.")
        return None

    if len(img.shape) != 2:
        print("HATA: Histogram eşitleme için giriş görüntüsü gri tonlamalı olmalıdır.")
        return None

    hist = np.bincount(img.flatten(), minlength=256)

    cdf = hist.cumsum()
    cdf_normalized = cdf * 255 / cdf[-1]

    equalized_img = cdf_normalized[img.flatten()].reshape(img.shape).astype(np.uint8)

    return equalized_img
