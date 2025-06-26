import numpy as np

def histogram_stretching(img):
    """
    Görüntünün her kanalını ayrı ayrı 0-255 aralığına esnetir (kontrast artırır).
    """
    if img is None:
        print("HATA: Histogram germe işlemi için geçerli bir görüntü bulunamadı.")
        return None

    stretched = np.zeros_like(img)

    if len(img.shape) == 2:
        min_val = np.min(img)
        max_val = np.max(img)
        if max_val - min_val == 0:
            return img
        stretched = 255 * (img - min_val) / (max_val - min_val)
        stretched = stretched.astype(np.uint8)

    elif len(img.shape) == 3:
        for i in range(3):
            channel = img[:, :, i]
            min_val = np.min(channel)
            max_val = np.max(channel)
            if max_val - min_val != 0:
                stretched[:, :, i] = 255 * (channel - min_val) / (max_val - min_val)
        stretched = stretched.astype(np.uint8)

    return stretched
