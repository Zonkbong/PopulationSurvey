import streamlit as st


st.set_page_config(
    page_title="Badan Pusat Statik"
)

st.title("Table Page")


tab1, tab2 = st.tabs(["2010", "2020"])


tab1.subheader("Jumlah dan Distribusi Penduduk Tahun 2010")


tab2.subheader("Jumlah dan Distribusi Penduduk Tahun 2020")

table_html = "<table>\n"
table_html += "  <tr>\n"
table_html += "    <th>Nomor</th>\n"
table_html += "    <th><center>Dataset</center></th>\t"
table_html += "    <th>Lihat Data</th>\n"
table_html += "  </tr>\n"

table_html += "     <td>1</td>\n"
table_html += "     <td>Penduduk yang Pindah menurut Wilayah dan Jenis Kelamin</td>\n"
table_html += "     <td><button>Lihat Data</button></td>\n"
table_html += "  </tr>\n"

table_html += "     <td>2</td>\n"
table_html += "     <td>Penduduk menurut Wilayah, Kelompok Umur, dan Jenis Kelamin</td>\n"
table_html += "     <td><button>Lihat Data</button></td>\n"
table_html += "  </tr>\n"

table_html += "     <td>3</td>\n"
table_html += "     <td>Penduduk menurut Wilayah, Klasifikasi Generasi</td>\n"
table_html += "     <td><button>Lihat Data</button></td>\n"
table_html += "  </tr>\n"

table_html += "     <td>4</td>\n"
table_html += "     <td>Penduduk Menurut  Kesesuaian Alamat KK dengan Domisili</td>\n"
table_html += "     <td><button>Lihat Data</button></td>\n"
table_html += "  </tr>\n"   

table_html += "     <td>5</td>\n"
table_html += "     <td>Penduduk menurut Wilayah dan Jenis Kelamin</td>\n"
table_html += "     <td><button>Lihat Data</button></td>\n"
table_html += "  </tr>\n"   

table_html += "</table>"
st.markdown(table_html, unsafe_allow_html=True)