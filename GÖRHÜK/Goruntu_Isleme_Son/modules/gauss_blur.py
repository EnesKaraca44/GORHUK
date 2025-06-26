import numpy as np

def gaussian_kernel(size, sigma=1):
    """
    Gaussian kernel üretir.
    """
    ax = np.arange(-size // 2 + 1., size // 2 + 1.)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2. * sigma**2))
    return kernel / np.sum(kernel)

def apply_convolution(image, kernel):
    """
    Verilen kernel ile görüntü üzerinde convolution uygular.
    """
    pad = kernel.shape[0] // 2
    if len(image.shape) == 3:
        padded_image = np.pad(image, ((pad, pad), (pad, pad), (0, 0)), mode='edge')
        result = np.zeros_like(image)

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                for c in range(3):
                    region = padded_image[i:i+kernel.shape[0], j:j+kernel.shape[1], c]
                    result[i, j, c] = np.sum(region * kernel)
    else:
        padded_image = np.pad(image, pad, mode='edge')
        result = np.zeros_like(image)

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                region = padded_image[i:i+kernel.shape[0], j:j+kernel.shape[1]]
                result[i, j] = np.sum(region * kernel)

    return result.astype(np.uint8)

def gaussian_blur(image, kernel_size=5, sigma=1):
    """
    Gaussian Blur uygular.
    """
    kernel = gaussian_kernel(kernel_size, sigma)
    return apply_convolution(image, kernel)
