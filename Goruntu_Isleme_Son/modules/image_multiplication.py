import numpy as np
from modules.load_image import load_image

def image_multiplication(img1, img2_path='images/lena.png'):
    """
    İki görüntüyü piksel piksel çarpar.
    Kullanıcı tarafından yüklenen görüntü ile sabit 'lena.png' dosyasını kullanır.
    """
    if img1 is None:
        print("HATA: Çarpma için geçerli bir birinci görüntü bulunamadı.")
        return None

    img2 = load_image(img2_path)
    if img2 is None:
        print("HATA: İkinci görüntü (lena.png) bulunamadı.")
        return None

    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]

    if (h1, w1) != (h2, w2):
        zoom_factor_h = h1 / h2
        zoom_factor_w = w1 / w2

        img2_resized = np.zeros_like(img1)

        for i in range(h1):
            for j in range(w1):
                img2_resized[i, j] = img2[min(int(i / zoom_factor_h), h2 - 1), min(int(j / zoom_factor_w), w2 - 1)]
    else:
        img2_resized = img2

    multiplied = (img1.astype(np.float32) * img2_resized.astype(np.float32)) / 255.0
    multiplied = np.clip(multiplied, 0, 255).astype(np.uint8)

    return multiplied
