import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Badan Pusat Statistik"
)

image =Image.open('peta.png')

st.title("Sensus Data Penduduk")

st.image(image, caption='Peta Indonesia')

st.header("Jumlah dan Distribusi Penduduk")

text ="Jumlah Penduduk Indonesia pada tahun 2010 adalah sebanyak 237.641.326 jiwa,yang mencakup mereka yang bertempat tinggal di daerah perkotaan sebanyak 118.320.256dan di daerah perdesaan sebanyak 119.321.070.Persebaran penduduk menurut jenis kelamin adalah 119.630.913 untuk penduduk laki-laki dan 118.010.413 untuk penduduk perempuan."

st.caption(text)








