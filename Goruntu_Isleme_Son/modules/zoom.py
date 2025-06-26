import numpy as np

def zoom_in(image, scale=2):
    """
    Görüntüyü yakınlaştırır (zoom in).
    Ölçek katsayısı kadar büyütür.
    """
    h, w = image.shape[:2]
    new_h, new_w = h * scale, w * scale

    if len(image.shape) == 3:
        result = np.zeros((new_h, new_w, image.shape[2]), dtype=image.dtype)
    else:
        result = np.zeros((new_h, new_w), dtype=image.dtype)

    for i in range(new_h):
        for j in range(new_w):
            result[i, j] = image[i // scale, j // scale]

    return result

def zoom_out(image, scale=2):
    """
    Görüntüyü uzaklaştırır (zoom out).
    Ölçek katsayısı kadar küçültür.
    """
    h, w = image.shape[:2]
    new_h, new_w = h // scale, w // scale

    if len(image.shape) == 3:
        result = np.zeros((new_h, new_w, image.shape[2]), dtype=np.uint8)
        for i in range(new_h):
            for j in range(new_w):
                block = image[i*scale:(i+1)*scale, j*scale:(j+1)*scale, :]
                result[i, j] = np.mean(block, axis=(0, 1))
    else:
        result = np.zeros((new_h, new_w), dtype=np.uint8)
        for i in range(new_h):
            for j in range(new_w):
                block = image[i*scale:(i+1)*scale, j*scale:(j+1)*scale]
                result[i, j] = np.mean(block)

    return result
