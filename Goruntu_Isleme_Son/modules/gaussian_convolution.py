import numpy as np

def gaussian_kernel(size=3, sigma=1):
    """
    Verilen boyut ve sigma ile bir Gaussian kernel üretir.
    """
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return kernel / np.sum(kernel)

def apply_convolution(img, kernel):
    """
    Görüntü üzerine verilen çekirdek ile konvolüsyon uygular.
    """
    if len(img.shape) == 2:
        img = img[:, :, np.newaxis]

    height, width, channels = img.shape
    k = kernel.shape[0] // 2

    padded = np.pad(img, ((k, k), (k, k), (0, 0)), mode='reflect')
    new_img = np.zeros_like(img)

    for y in range(height):
        for x in range(width):
            for c in range(channels):
                region = padded[y:y+kernel.shape[0], x:x+kernel.shape[1], c]
                new_value = np.sum(region * kernel)
                new_img[y, x, c] = np.clip(new_value, 0, 255)

    return new_img.squeeze().astype(np.uint8)

def gaussian_convolution(img):
    """
    Görüntüye Gaussian blur uygular (elle konvolüsyon).
    """
    if img is None:
        print("HATA: Gaussian konvolüsyon için geçerli bir görüntü bulunamadı.")
        return None

    kernel = gaussian_kernel(size=5, sigma=1)
    blurred_img = apply_convolution(img, kernel)
    return blurred_img
