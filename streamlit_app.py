import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder # scikit-learn
from pathlib import Path

# Show title and description.
st.title("📄 Superhost prediction by The Golden Gate")
st.write("AirBnb adalah sebuah platform yang menyediakan pemilik properti (host) untuk menyewakan property kepada tamu atau penyewa.")
st.write("Aplikasi ini dapat memprediksi pemilik properti dengan masukan atau input yang sudah sediakan dengan 23 kolom.")
st.write("**User bisa melihat contoh pada tab bagian *'Example'* untuk melihat contoh data dan hasil prediksinya**")

model_path = Path(__file__).parent / 'Gradient_Boosting_Classifier_RandomOverSampling.pkl' 

df = pd.read_csv('https://raw.githubusercontent.com/the-goldengate/web-api-superhost/refs/heads/main/data_example_2.0.csv', delimiter=";")

with open(model_path, 'rb') as file:
    model = pickle.load(file)

def model_output(model, data):
    df_encoded, encoders = encode_categorical_columns(data)

    # **Pastikan model yang di-load benar-benar objek, bukan string**
    if not hasattr(model, "predict"):
        st.error("Model tidak valid! Pastikan file .pkl adalah model yang sudah dilatih.")
    else:
        # **Melakukan prediksi**
        info = []
        predictions = model.predict(df_encoded)
        prediction_proba = model.predict_proba(df_encoded)[:, 1]  # Ambil probabilitas kelas "Superhost"

        # Buat kolom hasil prediksi
        data["Superhost Probability"] = prediction_proba
        data["Superhost Probability (%)"] = prediction_proba * 100 
        data["Superhost Probability (%)"] = data["Superhost Probability (%)"].apply(lambda x: f"{x:.1f}%")
        data["Superhost Status"] = data["Superhost Probability"].apply(lambda x: "Superhost" if x >= 0.396 else "Bukan Superhost")
        data["Superhost Probability"] = data["Superhost Probability"].apply(lambda x: f"{x:.3f}")

        hasil_prediksi = data[["Superhost Probability", "Superhost Probability (%)", "Superhost Status", ]]

        # Menampilkan hasil prediksi
        st.write("### Prediction")
        st.write("Model ini menggunakan threshold 39.6% untuk menentukan status Superhost berdasarkan probabilitas dari prediksi")
        st.dataframe(hasil_prediksi)

        if hasattr(model, 'feature_importances_'):
            st.subheader("Feature Importances")
            st.write("Fitur penting yang digunakan dalam prediksi")
            try:
                feature_names = model.feature_names_in_ #requires sklearn 1.2+
                importances = model.feature_importances_
                feature_importance_info = [{"Feature": feature, "Importance": f"{importance * 100:.1f}%"} for feature, importance in zip(feature_names, importances)]
            except AttributeError:
                feature_importance_info = [{"Feature Importances": str(model.feature_importances_)}]
            st.dataframe(pd.DataFrame(feature_importance_info))

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

# Fungsi untuk melakukan Label Encoding
def encode_categorical_columns(df):
    label_encoders = {}
    for col in df.select_dtypes(include=['object', 'category', 'bool']).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    return df, label_encoders

tab1, tab2 = st.tabs(["Test", "Example"])

with tab1:
    st.header("CSV Input")
    uploaded_file = st.file_uploader("Upload a document (.csv)", type=(["csv"]))
    if uploaded_file is not None:
        # Membaca CSV menjadi DataFrame
        df_uploaded = pd.read_csv(uploaded_file, delimiter=";")
        
        # Menampilkan data yang telah diunggah
        st.write("### Preview data yang diunggah:")
        st.dataframe(df_uploaded)
        model_output(model, df_uploaded)
            
with tab2:
    st.header("Example Data")
    st.write("Disini ada 10 baris data yang diuji coba untuk diprediksi")
    st.dataframe(df)
    model_output(model, df)
    output_model = st.button("Model Information")
    if output_model:
        st.write(f"**Model Used:** {type(model).__name__}")
        if hasattr(model, 'get_params'):
            params_info = [{"Parameter": key, "Value": value} for key, value in model.get_params().items()]
            if params_info:
                st.subheader("Model Parameters")
                st.dataframe(pd.DataFrame(params_info))

    

        
