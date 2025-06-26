import numpy as np

def color_space_conversion(img):
    """
    BGR formatındaki bir görüntüyü HSV formatına dönüştürür.
    """
    if img is None:
        print("HATA: Renk uzayı dönüşümü için geçerli bir görüntü bulunamadı.")
        return None

    img = img.astype('float32') / 255.0
    B, G, R = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    Cmax = np.max(img, axis=2)
    Cmin = np.min(img, axis=2)
    delta = Cmax - Cmin

    H = np.zeros_like(Cmax)

    mask = delta != 0
    idx = (Cmax == R) & mask
    H[idx] = (60 * ((G[idx] - B[idx]) / delta[idx]) + 0) % 360

    idx = (Cmax == G) & mask
    H[idx] = (60 * ((B[idx] - R[idx]) / delta[idx]) + 120) % 360

    idx = (Cmax == B) & mask
    H[idx] = (60 * ((R[idx] - G[idx]) / delta[idx]) + 240) % 360

    H[delta == 0] = 0

    S = np.zeros_like(Cmax)
    S[Cmax != 0] = delta[Cmax != 0] / Cmax[Cmax != 0]

    V = Cmax

    hsv = np.stack([H / 2, S * 255, V * 255], axis=2).astype(np.uint8)

    return hsv
