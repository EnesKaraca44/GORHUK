import numpy as np

def mean_filter(image, kernel_size=3):
    """
    Ortalama filtresi uygular (Mean Filter).
    """
    pad = kernel_size // 2
    if len(image.shape) == 3:
        padded_image = np.pad(image, ((pad, pad), (pad, pad), (0, 0)), mode='edge')
        result = np.zeros_like(image)

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                for c in range(3):
                    region = padded_image[i:i+kernel_size, j:j+kernel_size, c]
                    result[i, j, c] = np.mean(region)
    else:
        padded_image = np.pad(image, pad, mode='edge')
        result = np.zeros_like(image)

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                region = padded_image[i:i+kernel_size, j:j+kernel_size]
                result[i, j] = np.mean(region)

    return result.astype(np.uint8)
