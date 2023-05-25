import streamlit as st
import pandas as pd
from getAPI import GetAPI


getAPI = GetAPI()
getAPI.set_url = 'sp2020/5/1/3'

table_html = "<table>\n"
table_html += "  <tr>\n"
table_html += "    <th>Nama Wilayah</th>\n"
table_html += "    <th>Nilai</th>\n"
table_html += "  </tr>\n"

sortData = {}
for row in getAPI.getResponse("data"):
    sortedValue = row['nama_wilayah']
    if sortedValue not in sortData:
        sortData[sortedValue] = []
    sortData[sortedValue].append(row['nilai'])

for sortedValue, values in sortData.items():
    table_html += "  <tr>\n"
    table_html += f"    <td rowspan={len(values)}>{sortedValue}</td>\n"
    table_html += f"    <td>{values[0]}</td>\n"
    table_html += "  </tr>\n"

    for value in values[1:]:
        table_html += "  <tr>\n"
        table_html += f"    <td>{value}</td>\n"
        table_html += "  </tr>\n"

table_html += "</table>"
st.markdown(table_html, unsafe_allow_html=True)