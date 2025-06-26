from modules.dilation import dilation
from modules.erosion import erosion

def closing(img, kernel_size=3):
    """
    Kapanma (Closing): Dilation + Erosion uygular.
    """
    if img is None:
        print("HATA: Kapanma işlemi için geçerli bir görüntü bulunamadı.")
        return None

    if kernel_size % 2 == 0:
        print("HATA: Kernel boyutu tek sayı olmalıdır.")
        return None

    dilated = dilation(img, kernel_size)
    closed = erosion(dilated, kernel_size)
    return closed
