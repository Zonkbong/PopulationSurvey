import streamlit as st

st.set_page_config(
    page_title="Badan Pusat Statik"
)

st.title("Chart Page")

tab1, tab2 = st.tabs(["2010", "2020"])
with tab1:
    tab1.subheader("Jumlah dan Distribusi Penduduk Tahun 2010")
    table_html = "<table>\n"
    table_html += "  <tr>\n"
    table_html += "    <th>Nomor</th>\n"
    table_html += "    <th><center>Dataset</center></th>\t"
    table_html += "    <th>Lihat Data</th>\n"
    table_html += "  </tr>\n"

    table_html += "     <td>1</td>\n"
    table_html += "     <td>Penduduk Menurut Wilayah dan Status Kewarganegaraan, INDONESIA, Tahun 2010</td>\n"
    table_html += "     <td><a href=https://www.google.com><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>2</td>\n"
    table_html += "     <td>Penduduk Menurut Kelompok Umur dan Status Kewarganegaraan, INDONESIA, Tahun 2010</td>\n"
    table_html += "     <td><a href=https://www.google.com><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>3</td>\n"
    table_html += "     <td>Penduduk Menurut Wilayah dan Agama yang Dianut, INDONESIA, Tahun 2010</td>\n"
    table_html += "     <td><a href=https://www.google.com><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>4</td>\n"
    table_html += "     <td>Penduduk Menurut Kelompok Umur dan Agama yang Dianut, INDONESIA, Tahun 2010</td>\n"
    table_html += "     <td><a href=https://www.google.com><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>5</td>\n"
    table_html += "     <td>Penduduk Menurut Wilayah, Daerah Perkotaan/Perdesaan, dan Jenis Kelamin, INDONESIA, Tahun 2010</td>\n"
    table_html += "     <td><a href=https://www.google.com><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "</table>"
    st.markdown(table_html, unsafe_allow_html=True)

with tab2:
    tab2.subheader("Jumlah dan Distribusi Penduduk Tahun 2020")
    table_html = "<table>\n"
    table_html += "  <tr>\n"
    table_html += "    <th>Nomor</th>\n"
    table_html += "    <th><center>Dataset</center></th>\t"
    table_html += "    <th>Lihat Data</th>\n"
    table_html += "  </tr>\n"

    table_html += "     <td>1</td>\n"
    table_html += "     <td>Jumlah Penduduk Menurut Wilayah, Kesesuaian Alamat KK dengan Domisili, dan Jenis Kelamin, INDONESIA, Tahun 2020</td>\n"
    table_html += "     <td><a href=https://www.google.com><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>2</td>\n"
    table_html += "     <td>Jumlah Penduduk yang Pindah Menurut Wilayah dan Jenis Kelamin, INDONESIA, Tahun 2020</td>\n"
    table_html += "     <td><a href=https://www.google.com><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>3</td>\n"
    table_html += "     <td>Jumlah Penduduk Menurut Wilayah, Kelompok Umur, dan Jenis Kelamin, INDONESIA, Tahun 2020</td>\n"
    table_html += "     <td><a href=https://www.google.com><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>4</td>\n"
    table_html += "     <td>Jumlah Penduduk menurut Wilayah, Klasifikasi Generasi, dan Jenis Kelamin, INDONESIA, Tahun 2020</td>\n"
    table_html += "     <td><a href=https://www.google.com><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>5</td>\n"
    table_html += "     <td>Jumlah Penduduk menurut Wilayah dan Jenis Kelamin, INDONESIA, Tahun 2020</td>\n"
    table_html += "     <td><a href=https://www.google.com><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "</table>"
    st.markdown(table_html, unsafe_allow_html=True)