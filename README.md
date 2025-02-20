# **📝 Aplikasi Prediksi Superhost AirBnb - by The Golden Gate**

Aplikasi web ini menggunakan model machine learning untuk memprediksi status "Superhost" dari data AirBnb. Dibangun dengan Streamlit, aplikasi ini menyediakan fitur untuk mengunggah data CSV dan melihat hasil prediksi.

## **💻 Feature Web Application**

- Prediksi Status Superhost: Menggunakan model Gradient Boosting Classifier yang telah dilatih untuk memprediksi apakah seorang host akan menjadi Superhost.
- Unggah Data CSV: Memungkinkan pengguna untuk mengunggah file CSV yang berisi data AirBnb mereka.
- Tampilan Hasil Prediksi: Menampilkan probabilitas dan status prediksi (Superhost/Bukan Superhost) dalam format tabel.
- Informasi Model: Menampilkan detail model yang digunakan, termasuk tipe model dan parameter-parameternya.
- Feature Importances: Menampilkan fitur-fitur yang paling berpengaruh dalam prediksi.
- Contoh Data: Menyediakan data contoh untuk demonstrasi dan pemahaman cara kerja aplikasi.

📌
**✅ Members of The Golden gate ✅**

## How to run it on your own machine

1. Clone Repository

   ```
   git clone https://github.com/the-goldengate/web-api-superhost.git
   ```

2. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

3. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

## File Model
- `Gradient_Boosting_Classifier_RandomOverSampling.pkl`: Model machine learning yang digunakan untuk prediksi.