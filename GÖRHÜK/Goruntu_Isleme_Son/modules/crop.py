def crop_image(img):
    """
    Görüntünün merkezinden %50'lik bir alanı kırpar.
    """
    if img is None:
        print("HATA: Kırpma işlemi için geçerli bir görüntü bulunamadı.")
        return None

    height, width = img.shape[:2]

    new_height = height // 2
    new_width = width // 2

    start_row = (height - new_height) // 2
    start_col = (width - new_width) // 2

    cropped = img[start_row:start_row+new_height, start_col:start_col+new_width]

    return cropped
