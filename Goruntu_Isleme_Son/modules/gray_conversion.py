import numpy as np

def gray_conversion(image):
    if len(image.shape) == 3 and image.shape[2] == 3:
        gray = (0.299 * image[:, :, 0] +
                0.587 * image[:, :, 1] +
                0.114 * image[:, :, 2]).astype(np.uint8)
        return gray
    else:
        return image
