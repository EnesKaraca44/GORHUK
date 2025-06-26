# GÖRHÜK - Görüntüye Hükmet
## Proje Hakkında

**GÖRHÜK**, Dijital Görüntü İşleme'nin temel kavramlarını interaktif bir ortamda denemek ve öğrenmek amacıyla geliştirilmiş bir projedir. Kullanıcıların bir görüntü yükleyerek üzerinde 20'den fazla farklı görüntü işleme operasyonu gerçekleştirmesine olanak tanır.

Uygulama, modüler bir yapıda tasarlanmış olup, tüm görüntü işleme fonksiyonları kendi modülleri içinde yer almaktadır. Bu, kodun okunabilirliğini ve yönetilebilirliğini artırmaktadır.

---

## Özellikler

Uygulama, aşağıdaki temel görüntü işleme operasyonlarını desteklemektedir:

*   **Temel Dönüşümler:**
    *   Gri ve Binary (Siyah-Beyaz) renk dönüşümleri
    *   Görüntüyü saat yönünde ve tersinde döndürme
    *   Görüntüyü interaktif olarak kırpma
    *   Görüntüyü yakınlaştırma ve uzaklaştırma

*   **Renk & Histogram İşlemleri:**
    *   Farklı renk uzaylarına (HSV vb.) dönüştürme
    *   Histogram Germe (Contrast Stretching)
    *   Histogram Eşitleme (Equalization)
    *   Parlaklık artırma/azaltma

*   **Filtreleme & Gürültü Giderme:**
    *   "Salt & Pepper" gürültüsü ekleme
    *   Ortalama (Mean) ve Medyan (Median) filtreleri ile gürültü temizleme
    *   Ortalama (Mean) ve Gauss (Gaussian) Blurring

*   **Morfolojik İşlemler:**
    *   Erozyon (Erosion) ve Genişleme (Dilation)
    *   Açma (Opening) ve Kapanma (Closing)

*   **İleri Seviye İşlemler:**
    *   Kenar Tespiti (Sobel Filtresi)
    *   Adaptif Eşikleme
    *   Görüntü Toplama ve Çarpma

---

## Kullanılan Teknolojiler

*   **Python 3.10**
*   **OpenCV:** Görüntü işleme operasyonları için ana kütüphane.
*   **Tkinter:** Masaüstü kullanıcı arayüzünü (GUI) oluşturmak için.
*   **Numpy:** OpenCV tarafından kullanılan temel matris ve dizi işlemleri için.

---

## Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler
*   [Python 3.8+](https://www.python.org/downloads/)
*   [Git](https://git-scm.com/downloads)

### Adımlar
1.  **Depoyu klonlayın:**
    ```bash
    git clone https://github.com/EnesKaraca44/GORHUK.git
    ```

2.  **Proje dizinine gidin:**
    ```bash
    cd GORHUK
    ```

3.  **Gerekli kütüphaneleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Uygulamayı çalıştırın:**
    ```bash
    python main.py
    ```

---

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakınız.
