import streamlit as st
from getAPI2010 import GetAPI

getAPI = GetAPI()
getAPI.set_url = '14/91622/3'

st.markdown("<h2 style='text-align: center;'>Penduduk Menurut Wilayah dan Status Kewarganegaraan, INDONESIA, Tahun 2010 </h2>", unsafe_allow_html=True)
st.write("\n\n")

table_html = "<table>\n"
table_html += "  <br>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Warga</th>\n"
table_html += "    <th><center>Negara</th>\n"
table_html += "    <th><center>Indonesia</th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Warga</th>\n"
table_html += "    <th><center>Negara</th>\n"
table_html += "    <th><center>Asing</th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Tidak</th>\n"
table_html += "    <th><center>Ditanyakan</th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "  </br>\n"
table_html += "  <tr>\n"
table_html += "    <th><center>Nama Provinsi</th>\n"
#Warga Negara Indonesia
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Perkotaan</th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Perdesaan</th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th><center></th>\n"

#Warga Negara Asing
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Perkotaan</th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Perdesaan</th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th><center></th>\n"

#Tidak Ditanyakan
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Perkotaan</th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Perdesaan</th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th><center></th>\n"

#Total
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Perkotaan</th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Perdesaan</th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th><center></th>\n"
table_html += "  </tr>\n"
table_html += "  <tr>\n"
table_html += "    <th></th>\n"
#Warga Negara Indonesia
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

#Warga Negara Asing
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

#Tidak ditanyakan
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

#Total
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