import streamlit as st
import pandas as pd
import joblib
import numpy as np

def handle_outliers(column):
    Q1 = np.percentile(column, 25)
    Q3 = np.percentile(column, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    column[column < lower_bound] = lower_bound
    column[column > upper_bound] = upper_bound
    return column


# Model ve veri yükleme
model_path = "food-delivery-time-estimation-project/streamlit_app/model.pkl"
data_path = "food-delivery-time-estimation-project/streamlit_app/dataset.pkl"

model_pipeline = joblib.load(model_path)
with open(data_path, "rb") as f:
    data = joblib.load(f)
try:
    model=joblib.load(model_path)
    st.success("Model başarıyla yüklendi")
except Exception as e:
    st.error(f"Model yüklenirken hata oluştu: {e}")
    st.stop()

# Başlık
st.title("📦 Hızlı Teslimat Süresi Tahmini")
st.write("Teslimat süresini tahmin etmek için aşağıdaki bilgileri girin.")

# Kategorik değerlerin Türkçe ve İngilizce eşlemesi
weather_dict = {'Rüzgarlı': 'Windy', 'Açık': 'Clear', 'Sisli': 'Foggy', 'Yağmurlu': 'Rainy', 'Karlı': 'Snowy'}
traffic_dict = {'Düşük': 'Low', 'Orta': 'Medium', 'Yüksek': 'High'}
time_of_day_dict = {'Öğle': 'Afternoon', 'Akşam': 'Evening', 'Gece': 'Night', 'Sabah': 'Morning'}
vehicle_type_dict = {'Scooter': 'Skuter', 'Motor': 'Bike', 'Araba': 'Car'}

# Kullanıcı girdileri
distance_km = st.number_input("Mesafe (km)", min_value=0.1, value=5.0)
weather = st.selectbox("Hava Durumu", list(weather_dict.keys()))
traffic = st.selectbox("Trafik Seviyesi", list(traffic_dict.keys()))
time_of_day = st.selectbox("Günün Saati", list(time_of_day_dict.keys()))
vehicle_type = st.selectbox("Araç Türü", list(vehicle_type_dict.keys()))
preparation_time = st.number_input("Hazırlık Süresi (dk)", min_value=1, value=15)
courier_experience = st.number_input("Kurye Deneyimi (yıl)", min_value=0.0, value=1.0)

# Tahmin butonu
tahmin_butonu = st.button("Tahmin Yap")

if tahmin_butonu:
    # Kullanıcı girdilerini DataFrame formatına çevir ve Türkçe değerleri İngilizce'ye çevir
    input_data = pd.DataFrame({
        "Distance_km": [distance_km],
        "Weather": [weather_dict[weather]],  # Türkçe'den İngilizce'ye dönüşüm
        "Traffic_Level": [traffic_dict[traffic]],  # Türkçe'den İngilizce'ye dönüşüm
        "Time_of_Day": [time_of_day_dict[time_of_day]],  # Türkçe'den İngilizce'ye dönüşüm
        "Vehicle_Type": [vehicle_type_dict[vehicle_type]],  # Türkçe'den İngilizce'ye dönüşüm
        "Preparation_Time_min": [preparation_time],
        "Courier_Experience_yrs": [courier_experience]
    })


    # Modeli kullanarak tahmin yap
    predicted_time = model_pipeline.predict(input_data)[0]

    st.success(f"Tahmini Teslimat Süresi: {predicted_time:.2f} dakika")
