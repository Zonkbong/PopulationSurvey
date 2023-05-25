import streamlit as st
import pandas as pd
from getAPI import GetAPI


getAPI = GetAPI()
getAPI.set_url = 'sp2020/5/1/3'

getData = {}

for row in getAPI.getResponse("data"):
    namaWilayah = row["nama_wilayah"]
    if namaWilayah not in getData:
        getData[namaWilayah] = []
    getData[namaWilayah].append(row["nilai"])


data_frame = pd.DataFrame(getData)
st.table(data_frame)
