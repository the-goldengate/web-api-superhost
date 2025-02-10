import streamlit as st
from openai import OpenAI
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder # scikit-learn
from pathlib import Path

# Show title and description.
st.title("📄 Superhost prediction by The Golden Gate")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

# model_path = "https://raw.githubusercontent.com/the-goldengate/web-api-superhost/refs/heads/main/Gradient_Boosting_Classifier_SMOTE.pkl"
model_path = Path(__file__).parent / 'Gradient_Boosting_Classifier_SMOTE.pkl' 

df = pd.read_csv('https://raw.githubusercontent.com/the-goldengate/web-api-superhost/refs/heads/main/data.csv', delimiter=";")
ex = pd.read_csv('https://raw.githubusercontent.com/the-goldengate/web-api-superhost/refs/heads/main/example.csv', delimiter=";")

def load_model(pkl):
    with open(pkl, "rb") as file:
        pkl = pickle.load(file)
    return pkl

# Fungsi untuk melakukan Label Encoding
def encode_categorical_columns(df):
    label_encoders = {}
    for col in df.select_dtypes(include=['object', 'category', 'bool']).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    return df, label_encoders

tab1, tab2, tab3 = st.tabs(["Form", "CSV", "Example"])

with tab1:
    st.header("Form Input")
    st.write('**Ubah data sesuai yang diinginkan**')

    # Pastikan setiap user memiliki salinan data sendiri
    if "user_df" not in st.session_state:
        st.session_state.user_df = df.copy()

    # Menampilkan data editor hanya untuk user ini
    edited_df = st.data_editor(st.session_state.user_df)

    # Tombol untuk menyimpan perubahan (hanya berlaku untuk user ini)
    if st.button("Simpan Perubahan"):
        st.session_state.user_df = edited_df
        st.success("Perubahan berhasil disimpan!")
    

with tab2:
    st.header("CSV Input")
    uploaded_file = st.file_uploader("Upload a document (.csv)", type=(["csv"]))
    if uploaded_file is not None:
        # Membaca CSV menjadi DataFrame
        df_uploaded = pd.read_csv(uploaded_file, delimiter=";")
        
        # Menampilkan data yang telah diunggah
        st.write("### Preview data yang diunggah:")
        st.dataframe(df_uploaded)

with tab3:
    st.header("Examples")
    st.write('**Dummy Data**')
    st.dataframe(ex)

    model = load_model(model_path)
    df_encoded, encoders = encode_categorical_columns(ex)

    # **Pastikan model yang di-load benar-benar objek, bukan string**
    if not hasattr(model, "predict"):
        st.error("Model tidak valid! Pastikan file .pkl adalah model yang sudah dilatih.")
    else:
        # **Melakukan prediksi**
        predictions = model.predict(df_encoded)
        prediction_proba = model.predict_proba(df_encoded)[:, 1]  # Ambil probabilitas kelas "Superhost"

        # Buat kolom hasil prediksi
        ex["Superhost Probability"] = prediction_proba
        ex["Superhost Status"] = ex["Superhost Probability"].apply(lambda x: "Superhost" if x >= 0.5 else "Bukan Superhost")

        # Menampilkan hasil prediksi
        st.write("### Hasil Prediksi:")
        st.dataframe(ex[["Superhost Probability", "Superhost Status"]])
