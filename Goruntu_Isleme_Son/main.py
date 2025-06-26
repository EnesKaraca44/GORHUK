import cv2
import tkinter as tk
from tkinter import Label, Button, Frame

from modules.load_image import load_image_user as load_img
from modules.gray_conversion import gray_conversion
from modules.binary_conversion import binary_conversion
from modules.rotate import rotate_cw, rotate_ccw
from modules.crop import crop_image
from modules.zoom import zoom_in, zoom_out
from modules.color_space_conversion import color_space_conversion
from modules.histogram_stretching import histogram_stretching
from modules.histogram_equalization import histogram_equalization
from modules.image_addition import image_addition
from modules.image_multiplication import image_multiplication
from modules.increase_brightness import increase_brightness
from modules.gaussian_convolution import gaussian_convolution
from modules.adaptive_threshold import adaptive_threshold
from modules.sobel_edge_detection import sobel_edge_detection
from modules.add_noise import add_noise
from modules.mean_filter import mean_filter
from modules.median_filter import median_filter
from modules.mean_blur import mean_blur
from modules.gauss_blur import gaussian_blur
from modules.erosion import erosion
from modules.dilation import dilation
from modules.opening import opening
from modules.closing import closing

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Görüntüye Hükmet - GÖRHÜK")
        self.root.configure(bg="#e6f2ff")
        
        self.default_color = "#4da6ff"
        self.hover_color = "#80bfff"
        self.top_frame = Frame(root, bg="#e6f2ff")
        self.top_frame.pack(pady=1)

        button_style = {
            "width": 20,
            "bg": self.default_color,
            "fg": "white",
            "font": ("Helvetica", 10, "bold"),
            "relief": "ridge",
            "bd": 3
        }

        self.load_button = Button(self.top_frame, text="Görüntü Yükle", command=self.load_image, **button_style)
        self.load_button.pack(side="left", padx=10)
        self.add_hover(self.load_button)

        self.reset_button = Button(self.top_frame, text="Orijinal Görüntüye Dön", command=self.reset_image, **button_style)
        self.reset_button.pack(side="right", padx=10)
        self.add_hover(self.reset_button)

        self.image_label = Label(root, text="Görüntü burada gösterilecek", bg="gray", bd=3, relief="groove")
        self.image_label.pack(pady=1)

        self.button_frame = Frame(root, bg="#e6f2ff")
        self.button_frame.pack(pady=1)

        self.original_image = None
        self.display_image = None

        self.create_buttons(button_style)

    def add_hover(self, button):
        button.bind("<Enter>", lambda e: button.config(bg=self.hover_color))
        button.bind("<Leave>", lambda e: button.config(bg=self.default_color))

    def create_buttons(self, style):
        categories = {
            "Dönüşümler": [
                ("Gri Dönüştür", self.convert_to_gray),
                ("Binary Dönüştür", self.binary_conversion),
                ("Döndür (Saat Yönü)", self.rotate_cw),
                ("Döndür (Saat Tersi)", self.rotate_ccw),
                ("Kırp", self.crop_image),
                ("Yaklaştır", self.zoom_in),
                ("Uzaklaştır", self.zoom_out),
            ],
            "Renk İşlemleri": [
                ("Renk Uzayı Dönüştür", self.color_space_conversion),
                ("Histogram Germe", self.histogram_stretching),
                ("Histogram Eşitleme", self.histogram_equalization),
                ("Parlaklık Artır", self.increase_brightness),
            ],
            "Gürültü İşlemleri": [
                ("Gürültü Ekle (Salt & Pepper)", self.add_noise),
                ("Mean Filtre ile Temizle", self.mean_filter),
                ("Median Filtre ile Temizle", self.median_filter),
            ],
            "Blurring İşlemleri": [
                ("Ortalama Blurring", self.mean_blur),
                ("Gauss Blurring", self.gauss_blur),
                ("Konvolüsyon (Gauss)", self.gaussian_convolution),
            ],
            "Morfoloji İşlemleri": [
                ("Erozyon", self.apply_erosion),
                ("Genişleme", self.apply_dilation),
                ("Açılma", self.apply_opening),
                ("Kapanma", self.apply_closing),
            ],
            "İleri İşlemler": [
                ("Resim Toplama", self.image_addition),
                ("Resim Çarpma", self.image_multiplication),
                ("Adaptif Eşikleme", self.adaptive_threshold),
                ("Kenar Bulma (Sobel)", self.sobel_edge_detection),
            ]
        }

        for cat_idx, (category, actions) in enumerate(categories.items()):
            cat_label = Label(self.button_frame, text=category, bg="#e6f2ff", font=("Helvetica", 11, "bold"))
            cat_label.grid(row=cat_idx*10, column=0, columnspan=4, pady=(5))

            for idx, (text, command) in enumerate(actions):
                row = cat_idx*10 + (idx//4) + 1
                col = idx % 4
                btn = Button(self.button_frame, text=text, command=command, **style)
                btn.grid(row=row, column=col, padx=5, pady=5)
                self.add_hover(btn)
   
    def load_image(self):
        img = load_img()
        if img is not None:
            self.original_image = img
            self.display_image = img.copy()
            self.show_image(self.display_image)

    def reset_image(self):
        if self.original_image is not None:
            self.display_image = self.original_image.copy()
            self.show_image(self.display_image)

    def show_image(self, img_cv):
        img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        max_size = 400
        height, width = img_rgb.shape[:2]

        if height > max_size or width > max_size:
            if height > width:
                scale = max_size / height
            else:
                scale = max_size / width
            new_width = int(width * scale)
            new_height = int(height * scale)
            img_rgb = cv2.resize(img_rgb, (new_width, new_height))

        is_success, buffer = cv2.imencode(".png", img_rgb)
        if is_success:
            img_bytes = buffer.tobytes()
            img_tk = tk.PhotoImage(data=img_bytes)
            self.image_label.configure(image=img_tk)
            self.image_label.image = img_tk

    def convert_to_gray(self):
        if self.display_image is not None:
            gray_img = gray_conversion(self.display_image)
            if gray_img is not None:
                gray_img_bgr = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
                self.display_image = gray_img_bgr
                self.show_image(self.display_image)

    def binary_conversion(self):
        if self.display_image is not None:
            gray_img = gray_conversion(self.display_image)

            binary_img = binary_conversion(gray_img)

            if binary_img is not None:
                binary_img_bgr = cv2.cvtColor(binary_img, cv2.COLOR_GRAY2BGR)
                self.display_image = binary_img_bgr
                self.show_image(self.display_image)


    def rotate_cw(self):
        if self.display_image is not None:
            rotated_img = rotate_cw(self.display_image)
            if rotated_img is not None:
                self.display_image = rotated_img
                self.show_image(self.display_image)

    def rotate_ccw(self):
        if self.display_image is not None:
            rotated_img = rotate_ccw(self.display_image)
            if rotated_img is not None:
                self.display_image = rotated_img
                self.show_image(self.display_image)

    def crop_image(self):
        if self.display_image is not None:
            cropped_img = crop_image(self.display_image)
            if cropped_img is not None:
                self.display_image = cropped_img
                self.show_image(self.display_image)

    def zoom_in(self):
        if self.display_image is not None:
            zoomed_img = zoom_in(self.display_image)
            if zoomed_img is not None:
                self.display_image = zoomed_img
                self.show_image(self.display_image)

    def zoom_out(self):
        if self.display_image is not None:
            zoomed_img = zoom_out(self.display_image)
            if zoomed_img is not None:
                self.display_image = zoomed_img
                self.show_image(self.display_image)

    def color_space_conversion(self):
        if self.display_image is not None:
            hsv_img = color_space_conversion(self.display_image)
            if hsv_img is not None:
                self.display_image = hsv_img
                self.show_image(self.display_image)

    def histogram_stretching(self):
        if self.display_image is not None:
            stretched_img = histogram_stretching(self.display_image)
            if stretched_img is not None:
                self.display_image = stretched_img
                self.show_image(self.display_image)

    def histogram_equalization(self):
        if self.display_image is not None:
            gray_img = gray_conversion(self.display_image)

            equalized_img = histogram_equalization(gray_img)

            if equalized_img is not None:
                equalized_img_bgr = cv2.cvtColor(equalized_img, cv2.COLOR_GRAY2BGR)
                self.display_image = equalized_img_bgr
                self.show_image(self.display_image)


    def image_addition(self):
        if self.display_image is not None:
            added_img = image_addition(self.display_image)
            if added_img is not None:
                self.display_image = added_img
                self.show_image(self.display_image)

    def image_multiplication(self):
        if self.display_image is not None:
            multiplied_img = image_multiplication(self.display_image)
            if multiplied_img is not None:
                self.display_image = multiplied_img
                self.show_image(self.display_image)

    def increase_brightness(self):
        if self.display_image is not None:
            bright_img = increase_brightness(self.display_image)
            if bright_img is not None:
                self.display_image = bright_img
                self.show_image(self.display_image)

    def gaussian_convolution(self):
        if self.display_image is not None:
            blurred_img = gaussian_convolution(self.display_image)
            if blurred_img is not None:
                self.display_image = blurred_img
                self.show_image(self.display_image)

    def adaptive_threshold(self):
        if self.display_image is not None:
            thresholded_img = adaptive_threshold(self.display_image)
            if thresholded_img is not None:
                thresholded_img_bgr = cv2.cvtColor(thresholded_img, cv2.COLOR_GRAY2BGR)
                self.display_image = thresholded_img_bgr
                self.show_image(self.display_image)

    def sobel_edge_detection(self):
        if self.display_image is not None:
            edge_img = sobel_edge_detection(self.display_image)
            if edge_img is not None:
                edge_img_bgr = cv2.cvtColor(edge_img, cv2.COLOR_GRAY2BGR)
                self.display_image = edge_img_bgr
                self.show_image(self.display_image)

    def add_noise(self):
        if self.display_image is not None:
            noisy_img = add_noise(self.display_image)
            if noisy_img is not None:
                self.display_image = noisy_img
                self.show_image(self.display_image)

    def mean_filter(self):
        if self.display_image is not None:
            filtered_img = mean_filter(self.display_image)
            if filtered_img is not None:
                self.display_image = filtered_img
                self.show_image(self.display_image)

    def median_filter(self):
        if self.display_image is not None:
            filtered_img = median_filter(self.display_image)
            if filtered_img is not None:
                self.display_image = filtered_img
                self.show_image(self.display_image)

    def mean_blur(self):
        if self.display_image is not None:
            blurred_img = mean_blur(self.display_image)
            if blurred_img is not None:
                self.display_image = blurred_img
                self.show_image(self.display_image)

    def gauss_blur(self):
        if self.display_image is not None:
            blurred_img = gaussian_blur(self.display_image)
            if blurred_img is not None:
                self.display_image = blurred_img
                self.show_image(self.display_image)

    def apply_erosion(self):
        if self.display_image is not None:
            eroded_img = erosion(self.display_image)
            if eroded_img is not None:
                if len(eroded_img.shape) == 2:
                    eroded_img_bgr = cv2.cvtColor(eroded_img, cv2.COLOR_GRAY2BGR)
                else:
                    eroded_img_bgr = eroded_img

                self.display_image = eroded_img_bgr
                self.show_image(self.display_image)

    def apply_dilation(self):
        if self.display_image is not None:
            dilated_img = dilation(self.display_image)
            if dilated_img is not None:
                if len(dilated_img.shape) == 2:
                    dilated_img_bgr = cv2.cvtColor(dilated_img, cv2.COLOR_GRAY2BGR)
                else:
                    dilated_img_bgr = dilated_img

                self.display_image = dilated_img_bgr
                self.show_image(self.display_image)

    def apply_opening(self):
        if self.display_image is not None:
            opened_img = opening(self.display_image)
            if opened_img is not None:
                if len(opened_img.shape) == 2:
                    opened_img_bgr = cv2.cvtColor(opened_img, cv2.COLOR_GRAY2BGR)
                else:
                    opened_img_bgr = opened_img

                self.display_image = opened_img_bgr
                self.show_image(self.display_image)

    def apply_closing(self):
        if self.display_image is not None:
            closed_img = closing(self.display_image)
            if closed_img is not None:
                if len(closed_img.shape) == 2:
                    closed_img_bgr = cv2.cvtColor(closed_img, cv2.COLOR_GRAY2BGR)
                else:
                    closed_img_bgr = closed_img

                self.display_image = closed_img_bgr
                self.show_image(self.display_image)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()
