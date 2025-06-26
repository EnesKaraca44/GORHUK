import numpy as np

def erosion(image, kernel_size=3):
    """
    Erosion işlemi uygular. (Minimum değer alır)
    """
    pad = kernel_size // 2
    padded_image = np.pad(image, pad, mode='edge')
    result = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i+kernel_size, j:j+kernel_size]
            result[i, j] = np.min(region)

    return result
