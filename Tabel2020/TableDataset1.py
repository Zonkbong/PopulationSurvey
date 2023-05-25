import streamlit as st
from getAPI2020 import GetAPI

getAPI = GetAPI()
getAPI.set_url = '5/1/3'

st.markdown("<h2 style='text-align: center;'>Jumlah Penduduk Menurut Wilayah, Kesesuaian Alamat KK dengan Domisili, dan Jenis Kelamin, INDONESIA, Tahun 2020</h2>", unsafe_allow_html=True)
st.write("\n\n")

table_html = "<table>\n"
table_html += "  <tr>\n"
table_html += "    <th><center>Nama Provinsi</th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Sesuai</th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Tidak Sesuai</th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th><center></th>\n"
table_html += "  </tr>\n"
table_html += "  <tr>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"
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