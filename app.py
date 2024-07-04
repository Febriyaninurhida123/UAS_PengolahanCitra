import streamlit as st
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
