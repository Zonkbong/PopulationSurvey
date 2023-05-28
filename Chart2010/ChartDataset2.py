import streamlit as st
import pandas as pd
from getAPI2010 import GetAPI

st.set_page_config(
    page_title="Badan Pusat Statistik"
)

getAPI = GetAPI()
getAPI.set_url = '13/91622/3'

st.markdown("<h2 style='text-align: center;'>Penduduk Menurut Kelompok Umur dan Status Kewarganegaraan Tahun 2010</h2>", unsafe_allow_html=True)
st.write("\n\n")

sortData = {}
for row in getAPI.getResponse("data"):
    sortedValue = row['nama_wilayah']
    if sortedValue not in sortData:
        sortData[sortedValue] = []
    sortData[sortedValue].append(row['nilai'])

provinsi = list(sortData.keys())
displayData = {k: sortData[k][8] for k in provinsi}
df = pd.DataFrame.from_dict(displayData, orient='index', columns=['Data'])
st.bar_chart(df)