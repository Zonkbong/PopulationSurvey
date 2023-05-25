import streamlit as st
from getAPI import GetAPI

getAPI = GetAPI()
getAPI.set_url = 'sp2020/5/1/3'

st.markdown("<h2 style='text-align: center;'> Jumlah Penduduk yang Pindah menurut Wilayah dan Jenis Kelamin</h2>", unsafe_allow_html=True)
st.write("\n\n")

table_html = "<table>\n"
table_html += "  <tr>\n"
table_html += "    <th><center>Nama Wilayah</th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Sesuai</th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Tidak Sesuai</th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th></th>\n"
table_html += "  </tr>\n"
table_html += "  <tr>\n"
table_html += "    <th></th>\n"
table_html += "    <th>Laki - Laki</th>\n"
table_html += "    <th>Perempuan</th>\n"
table_html += "    <th>Total</th>\n"
table_html += "    <th>Laki - Laki</th>\n"
table_html += "    <th>Perempuan</th>\n"
table_html += "    <th>Total</th>\n"
table_html += "    <th>Laki - Laki</th>\n"
table_html += "    <th>Perempuan</th>\n"
table_html += "    <th>Total</th>\n"
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