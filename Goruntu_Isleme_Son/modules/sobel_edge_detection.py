import numpy as np
from modules.gray_conversion import gray_conversion

def sobel_edge_detection(image):
    """
    Sobel Edge Detection uygular.
    """
    image = gray_conversion(image)

    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    sobel_y = np.array([[-1, -2, -1],
                        [ 0,  0,  0],
                        [ 1,  2,  1]])

    pad = 1
    padded_image = np.pad(image, pad, mode='edge')
    result = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i+3, j:j+3]

            gx = np.sum(region * sobel_x)
            gy = np.sum(region * sobel_y)

            magnitude = np.sqrt(gx**2 + gy**2)

            result[i, j] = np.clip(magnitude, 0, 255)

    return result.astype(np.uint8)
