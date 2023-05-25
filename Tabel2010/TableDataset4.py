import streamlit as st
from getAPI2010 import GetAPI

getAPI = GetAPI()
getAPI.set_url = '11/91622/3'

st.markdown("<h2 style='text-align: center;'>Penduduk Menurut Kelompok Umur dan Agama yang Dianut, INDONESIA, Tahun 2010 </h2>", unsafe_allow_html=True)
st.write("\n\n")

table_html = "<table>\n"
table_html += "  <br>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Islam</th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Kristen</th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Katolik</th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Hindu</th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Budha</th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Khong Hu Chu</th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Lainnya</th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th></th>\n"
table_html += "    <th><center>Tidak</th>\n"
table_html += "    <th><center>Terjawab</th>\n"
table_html += "    <th></th>\n"
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
#Islam
table_html += "    <th></th>\n"
table_html += "    <th><center>Perkotaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Perdesaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th></th>\n"

#Kristen
table_html += "    <th></th>\n"
table_html += "    <th><center>Perkotaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Perdesaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th></th>\n"

#Katolik
table_html += "    <th></th>\n"
table_html += "    <th><center>Perkotaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Perdesaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th></th>\n"

#Hindu
table_html += "    <th></th>\n"
table_html += "    <th><center>Perkotaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Perdesaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th></th>\n"

#Budha
table_html += "    <th></th>\n"
table_html += "    <th><center>Perkotaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Perdesaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th></th>\n"

#Khong Hu Chu
table_html += "    <th></th>\n"
table_html += "    <th><center>Perkotaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Perdesaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th></th>\n"

#Lainnya
table_html += "    <th></th>\n"
table_html += "    <th><center>Perkotaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Perdesaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th></th>\n"

#Tidak Terjawab
table_html += "    <th></th>\n"
table_html += "    <th><center>Perkotaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Perdesaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th></th>\n"


#Tidak ditanyakan
table_html += "    <th></th>\n"
table_html += "    <th><center>Perkotaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Perdesaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th></th>\n"

#Total
table_html += "    <th></th>\n"
table_html += "    <th><center>Perkotaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Perdesaan</th>\n"
table_html += "    <th></th>\n"

table_html += "    <th></th>\n"
table_html += "    <th><center>Total</th>\n"
table_html += "    <th></th>\n"
table_html += "  </tr>\n"

table_html += "  <tr>\n"
table_html += "    <th></th>\n"

#Islam
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

#Kristen
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

#katolik
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

#Hindu
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

#Budha
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

#Khong Hu Chu
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

#Lainnya
table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

table_html += "    <th><center>Laki - Laki</th>\n"
table_html += "    <th><center>Perempuan</th>\n"
table_html += "    <th><center>Total</th>\n"

#Tidak terjawab
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
    sortedValue = row['nama_item__kategori_1']
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