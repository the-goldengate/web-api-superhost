# **📝 Application Prediction Superhost AirBnb - by The Golden Gate**

Aplikasi web ini menggunakan model machine learning untuk memprediksi status **Superhost** dari data AirBnb. Dibangun dengan Streamlit, aplikasi ini menyediakan fitur untuk mengunggah data CSV dan melihat hasil prediksi.

## **Domain Demo Website Streamlit**

`https://superhost.streamlit.app/`

## **💻 Feature Web Application**

- **Prediksi Status Superhost:**
   Menggunakan model **Gradient Boosting Classifier** yang telah dilatih untuk memprediksi apakah seorang host akan menjadi **Superhost**.

- **Unggah Data CSV:**
   Pengguna dapat mengunggah file CSV yang berisi data AirBnb.

- **Tampilan Hasil Prediksi:** 
   Menampilkan probabilitas dan status prediksi (Superhost dan Bukan Superhost) dalam format tabel.

- **Informasi Model:** 
   Menampilkan detail model yang digunakan, termasuk tipe model dan parameter-parameternya.

- **Feature Importances:** 
   Menampilkan fitur-fitur yang paling berpengaruh dalam prediksi.

- **Contoh Data:** 
   Menyediakan data contoh untuk demonstrasi dan pemahaman cara kerja aplikasi.



## ⚙️ **How to run it on your own machine**

1. Clone Repositorinya

   ```
   git clone https://github.com/the-goldengate/web-api-superhost.git
   ```

2. Instal requirement.txt

   ```
   $ pip install -r requirements.txt
   ```

3. Jalankan aplikasi

   ```
   $ streamlit run streamlit_app.py
   ```

## 📂 **File Model**
`Gradient_Boosting_Classifier_RandomOverSampling.pkl`: Model machine learning yang digunakan untuk prediksi.

## 📌 **How to use it**
### **Unggah Data CSV (Tab "Test"):**
- Buka tab **Test**.
- Unggah file CSV dengan menekan tombol **Browse files**.
- Lihat pratinjau data yang diunggah.
- Hasil prediksi akan ditampilkan secara otomatis.

### **Lihat Data Contoh dan Hasil Prediksi (Tab "Example"):**
- Buka tab **Example**.
- Lihat data contoh yang disediakan.
- Lihat hasil prediksi untuk data contoh tersebut.
- Klik tombol **Model Information** untuk melihat detail model.

### **Memahami Hasil Prediksi:**
- **Superhost Probability**: Probabilitas menjadi Superhost (angka desimal).
- **Superhost Probability (%)**: Probabilitas dalam persentase.
- **Superhost Status**: Status prediksi (Superhost/Bukan Superhost).
- **Feature Importances**: Fitur-fitur yang paling berpengaruh dalam prediksi.

## 📲 **Web Application Overview on the "Example" Tab**
### `Bentuk Gambaran web pada preview data`

![gambar](https://github.com/user-attachments/assets/0b5c3aa3-1b62-4c4e-a183-d56b91976026)

## 📲 **Web Application Overview on the "Test" Tab**
### `Bentuk Gambaran web pada preview data`

![gambar](https://github.com/user-attachments/assets/aba29518-d13e-4a10-ba1a-014f614eff21)

## 📲 **Web Application Overview on Output Results**

### `Bentuk Gambaran hasil prediksi`

![gambar](https://github.com/user-attachments/assets/c5e28b95-fb01-4e73-998e-c921538acc7a)

### `Bentuk Gambaran hasil Feature Importances`

![gambar](https://github.com/user-attachments/assets/e5826e10-144d-490a-b6db-c365c2e6d41d)

### `Bentuk Gambaran hasil Informasi Model`

![gambar](https://github.com/user-attachments/assets/de2f46ef-a191-4871-a47d-bc7f56a4f9b6)

