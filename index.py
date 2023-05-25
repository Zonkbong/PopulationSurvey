import streamlit as st
from getAPI import GetAPI

getAPI = GetAPI()
getAPI.set_url = 'sp2020/5/1/3'

table_html = "<table>\n"
table_html += "  <tr>\n"
table_html += "    <th>Nama Wilayah</th>\n"
table_html += "    <th>Nilai 1</th>\n"
table_html += "    <th>Nilai 2</th>\n"
table_html += "    <th>Nilai 3</th>\n"
table_html += "    <th>Nilai 4</th>\n"
table_html += "    <th>Nilai 5</th>\n"
table_html += "    <th>Nilai 6</th>\n"
table_html += "    <th>Nilai 7</th>\n"
table_html += "    <th>Nilai 8</th>\n"
table_html += "    <th>Nilai 9</th>\n"
table_html += "  </tr>\n"

sortData = {}
for row in getAPI.getResponse("data"):
    sortedValue = row['nama_wilayah']
    if sortedValue not in sortData:
        sortData[sortedValue] = []
    sortData[sortedValue].append(row['nilai'])

for sortedValue, values in sortData.items():
    table_html += "  <tr>\n"
    table_html += f"    <td>{sortedValue}</td>\n"
    for value in values:
        table_html += f"      <td>{value}</td>\n"
    table_html += "  </tr>\n"

table_html += "</table>"
st.markdown(table_html, unsafe_allow_html=True)