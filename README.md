# UAS_PengolahanCitra
```
Alifia Ananda Putri (312210168)
Febriyani Nurhida (312210222)
TI.22.A2
```
# Jurnal 
[csit (2).docx](https://github.com/user-attachments/files/16094412/csit.2.docx)

# Pembacaan dan Konversi Warna Gambar
Pertama, gambar dibaca menggunakan OpenCV dan kemudian dikonversi dari format BGR (default OpenCV) ke RGB untuk keperluan visualisasi yang lebih tepat di matplotlib.

```import numpy as np
import matplotlib.pyplot as plt
import cv2
%matplotlib inline
```

# Membaca gambar sesuai dengan yang dimiliki
```image = cv2.imread('images/monarch.jpg')
```
# Mengubah warna menjadi RGB (dari BGR)
```image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
```
Langkah berikutnya adalah mengubah gambar menjadi susunan piksel 2D dengan masing-masing piksel memiliki 3 nilai warna (RGB).

# Membentuk ulang gambar menjadi susunan piksel 2D dengan 3 nilai warna (RGB)
```pixel_vals = image.reshape((-1, 3))
```
# Mengkonversikan ke tipe float
```pixel_vals = np.float32(pixel_vals)
```
Menentukan kriteria untuk algoritma K-Means agar berhenti berjalan setelah mencapai jumlah iterasi tertentu atau tingkat akurasi yang diinginkan, kemudian melaksanakan klasterisasi dengan jumlah klaster yang ditetapkan.

# Menentukan kriteria untuk algoritme berhenti berjalan
```criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
```
# Melakukan k-means clustering dengan jumlah cluster yang ditetapkan sebagai 3
```k = 3
retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
```

Setelah klasterisasi selesai, data dikonversi kembali ke nilai 8-bit dan hasil klasterisasi divisualisasikan dengan membentuk ulang data ke dimensi gambar asli.

# Mengonversi data menjadi nilai 8-bit
```centers = np.uint8(centers)
segmented_data = centers[labels.flatten()]
# Membentuk ulang data menjadi dimensi gambar asli
segmented_image = segmented_data.reshape((image.shape))
plt.imshow(segmented_image)
```
Melalui langkah-langkah di atas, gambar telah berhasil diklasterisasi menjadi tiga kelompok warna menggunakan algoritma K-Means. Proses ini melibatkan pembacaan gambar, pra-pengolahan, penerapan K-Means, dan visualisasi hasil.
![monarch](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/9cc03ead-f2b9-44c7-a252-9ca616faff30)
![monarch_after](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/cddfa039-78a2-4cb9-ab99-d177024ed188)

# Implementasi project streamlite 
	Aplikasi ini diimplementasikan menggunakan Streamlit untuk antarmuka pengguna dan OpenCV untuk pemrosesan gambar. Pengguna dapat mengatur jumlah cluster (kkk) menggunakan slider dan menekan tombol untuk menjalankan segmentasi. Hasil segmentasi ditampilkan dalam bentuk gambar yang telah dikelompokkan berdasarkan warna.

# Build App Klasterisasi Warna pada gambar
``` import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

def segment_image(image, k, max_iter=100, epsilon=0.85):
    # Ubah warna gambar dari RGB ke BGR untuk cv2
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    # Membentuk ulang gambar menjadi susunan piksel 2D dan 3 nilai warna (RGB)
    pixel_vals = image.reshape((-1, 3))

    # Mengkonversikan ke tipe float
    pixel_vals = np.float32(pixel_vals)

    # Menentukan kriteria agar algoritme berhenti berjalan
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, max_iter, epsilon)

    # Melakukan k-means clustering
    retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Mengonversi data menjadi nilai 8-bit
    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]

    # Membentuk ulang data menjadi dimensi gambar asli
    segmented_image = segmented_data.reshape((image.shape))

    # Ubah kembali warna gambar dari BGR ke RGB untuk ditampilkan
    segmented_image = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB)

    return segmented_image

st.title("Segmentasi Gambar Menggunakan K-Means Clustering")
st.write("Unggah gambar dan sesuaikan parameter untuk segmentasi gambar.")

# Unggah gambar
uploaded_file = st.file_uploader("Pilih file gambar", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = np.array(Image.open(uploaded_file))
    
    st.image(image, caption='Gambar Asli', use_column_width=True)
    
    # Slider untuk memilih jumlah cluster (k)
    k = st.slider("Jumlah Cluster (k)", min_value=2, max_value=10, value=3)
    
    # Tombol untuk menjalankan segmentasi
    if st.button("Segmentasikan Gambar"):
        segmented_image = segment_image(image, k)
        
        st.image(segmented_image, caption='Gambar Tersegmentasi', use_column_width=True)

# Menjalankan aplikasi Streamlit
if __name__ == '__main__':
    st.set_option('deprecation.showPyplotGlobalUse', False)
```

![hasilgambar](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/b1bbc32a-5c42-459f-82e9-f728404c1469)

## Hasil project Streamlite Klaterisasi Warna
![HasilKucing](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/dfa71f64-f214-4f8d-b266-d3fea6fe17d9)
![HasilKlepon](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/f253a196-9db9-4e53-a896-532566cc8044)
![HasilKetoprak](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/eb6011d1-f00d-41f6-bc47-791c6f920239)
![HasilDoshirak](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/5485f070-72e0-4ccd-a28c-d762f13494ae)
![HasilBistik](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/c3e72ab7-1baa-4a34-9b50-038f48edcef2)
![doshirak](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/a6f03a05-aa82-4c48-8268-1f72d4b31d9c)
![bistik](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/8a323a84-ffc1-4221-a180-2479129644f3)
![seblak](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/2a4c6779-2ee7-4000-a0d2-47eced172be2)
![monarch_after](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/390a04b1-052d-43ec-8b89-b37932885396)
![monarch](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/02642d57-6276-48cf-a057-07aa1965eecb)
![kucing](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/3936f82b-375a-4490-9068-d55e5f48f1a1)
![klepon](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/1bcdb188-7681-48e2-819e-2bcedc2a332e)
![ketoprak](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/ebe71a27-5c1f-4ca9-bc31-f163a225e4ef)
![HasilSeblak](https://github.com/Febriyaninurhida123/UAS_PengolahanCitra/assets/90132092/37f2352b-f956-4c35-b07b-6acab755783d)


