import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style="whitegrid")

#Load dataset
day_data = pd.read_csv("./dashboard/day_cleaned.csv")
hour_data = pd.read_csv("./dashboard/hour_cleaned.csv")



st.title("Dashboard Bike Sharing Dataset")

#Menampilkan beberapa baris dari dataset
st.header("Bike Sharing Dataset")
st.write(day_data.head())

#Analisis dan Insight
st.header("Insight")
st.write("1. Jumlah penyewaan lebih tinggi pada hari kerja.")
st.write("2. Penyewaan sepeda meningkat saat cuaca cerah.")

#Visualisasi Pengaruh Kondisi Cuaca
st.header("Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda")
weather_group = day_data.groupby(by="weathersit").agg({"cnt": "sum"})
fig1, ax1 = plt.subplots()
sns.barplot(x=weather_group.index, y='cnt', data=weather_group, palette='viridis', ax=ax1)
ax1.set_title('Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan')
ax1.set_xlabel('Kondisi Cuaca')
ax1.set_ylabel('Jumlah Penyewaan')
ax1.set_xticklabels(['Cerah', 'Berawan', 'Hujan Ringan', 'Hujan Berat'], rotation=45)
st.pyplot(fig1)

#Visualisasi Jumlah Penyewaan berdasarkan Hari
st.header("Jumlah Penyewaan Sepeda berdasarkan Hari dalam Seminggu")
weekday_group = day_data.groupby(by="weekday").agg({"cnt": "sum"})
fig2, ax2 = plt.subplots()
sns.barplot(x=weekday_group.index, y='cnt', data=weekday_group.reset_index(), palette='coolwarm', ax=ax2)
ax2.set_title('Jumlah Penyewaan berdasarkan Hari dalam Seminggu')
ax2.set_xlabel('Hari dalam Seminggu (0=Senin, 6=Minggu)')
ax2.set_ylabel('Jumlah Penyewaan')
ax2.set_xticklabels(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'], rotation=45)
st.pyplot(fig2)

st.header("Kesimpulan")
st.write("Cuaca sangat mempengaruhi jumlah penyewaan sepeda. Penyewaan paling tinggi saat cuaca cerah, jadi promosi saat cuaca baik bisa efektif.")
st.write("Pola penyewaan yang kuat pada hari kerja menunjukkan bahwa sepeda dapat menjadi solusi transportasi yang efisien.")

