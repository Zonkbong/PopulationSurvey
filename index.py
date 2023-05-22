import streamlit as st
from getAPI import GetAPI

getAPI = GetAPI()
getAPI.set_url = 'sp2020/2/1/3'

getData = {}

for row in getAPI.getResponse("data"):
    namaWilayah = row["nama_wilayah"]
    if namaWilayah not in getData:
        getData[namaWilayah] = []
    getData[namaWilayah].append(row["nilai"])

for itemWilayah, itemNilai in getData.items():
    st.write(itemWilayah, itemNilai)