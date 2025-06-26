import numpy as np

def mean_blur(img, kernel_size=5):
    """
    Görüntüye ortalama (mean) blurring uygular.
    """
    if img is None:
        print("HATA: Mean blurring için geçerli bir görüntü bulunamadı.")
        return None

    if kernel_size % 2 == 0:
        print("HATA: Kernel boyutu tek sayı olmalıdır.")
        return None

    if len(img.shape) == 2:
        img = img[:, :, np.newaxis]

    height, width, channels = img.shape
    k = kernel_size // 2

    padded = np.pad(img, ((k, k), (k, k), (0, 0)), mode='reflect')
    output = np.zeros_like(img)

    for y in range(height):
        for x in range(width):
            for c in range(channels):
                region = padded[y:y+kernel_size, x:x+kernel_size, c]
                output[y, x, c] = np.mean(region)

    return output.squeeze().astype(np.uint8)
