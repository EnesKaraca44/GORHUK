from modules.erosion import erosion
from modules.dilation import dilation

def opening(img, kernel_size=3):
    """
    Açılma (Opening): Erosion + Dilation uygular.
    """
    if img is None:
        print("HATA: Açılma işlemi için geçerli bir görüntü bulunamadı.")
        return None

    if kernel_size % 2 == 0:
        print("HATA: Kernel boyutu tek sayı olmalıdır.")
        return None

    eroded = erosion(img, kernel_size)
    opened = dilation(eroded, kernel_size)
    return opened
