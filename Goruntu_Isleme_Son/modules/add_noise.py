import numpy as np

def add_noise(img, amount=0.02):
    """
    Görüntüye salt & pepper (tuz ve karabiber) gürültüsü ekler.
    'amount' değeri gürültü oranını belirler.
    """
    if img is None:
        print("HATA: Gürültü ekleme için geçerli bir görüntü bulunamadı.")
        return None

    output = img.copy()

    total_pixels = img.shape[0] * img.shape[1]

    num_noise = int(total_pixels * amount)

    for _ in range(num_noise):
        y = np.random.randint(0, img.shape[0])
        x = np.random.randint(0, img.shape[1])

        if img.ndim == 2:
            output[y, x] = 0 if np.random.rand() < 0.5 else 255
        else:
            if np.random.rand() < 0.5:
                output[y, x] = [0, 0, 0]
            else:
                output[y, x] = [255, 255, 255]

    return output
