import streamlit as st
import pandas as pd
from getAPI2010 import GetAPI

getAPI = GetAPI()
getAPI.set_url = '12/91622/3'

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