import streamlit as st
import subprocess

st.set_page_config(
    page_title="Badan Pusat Statik"
)

st.title("Table Page")
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
    table_html += "     <td><a href=https://zonkbong-populationsurvey-tabel2010tabledataset1-n1hjdk.streamlit.app//><button> Lihat Data </button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>2</td>\n"
    table_html += "     <td>Penduduk Menurut Kelompok Umur dan Status Kewarganegaraan, INDONESIA, Tahun 2010</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-tabel2010tabledataset2-pfkjhv.streamlit.app//><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>3</td>\n"
    table_html += "     <td>Penduduk Menurut Wilayah dan Agama yang Dianut, INDONESIA, Tahun 2010</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-tabel2010tabledataset3-k23owc.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>4</td>\n"
    table_html += "     <td>Penduduk Menurut Kelompok Umur dan Agama yang Dianut, INDONESIA, Tahun 2010</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-tabel2010tabledataset4-kiuz43.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>5</td>\n"
    table_html += "     <td>Penduduk Menurut Wilayah, Daerah Perkotaan/Perdesaan, dan Jenis Kelamin, INDONESIA, Tahun 2010</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-tabel2010tabledataset5-5fk9mz.streamlit.app/><button>Lihat Data</button></a></td>"
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
    table_html += "     <td><a href=https://zonkbong-populationsurvey-tabel2020tabledataset1-sdhaw9.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>2</td>\n"
    table_html += "     <td>Jumlah Penduduk yang Pindah Menurut Wilayah dan Jenis Kelamin, INDONESIA, Tahun 2020</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-tabel2020tabledataset2-bainda.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>3</td>\n"
    table_html += "     <td>Jumlah Penduduk Menurut Wilayah, Kelompok Umur, dan Jenis Kelamin, INDONESIA, Tahun 2020</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-tabel2020tabledataset3-2m2ruu.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>4</td>\n"
    table_html += "     <td>Jumlah Penduduk menurut Wilayah, Klasifikasi Generasi, dan Jenis Kelamin, INDONESIA, Tahun 2020</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-tabel2020tabledataset4-wrfylf.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>5</td>\n"
    table_html += "     <td>Jumlah Penduduk menurut Wilayah dan Jenis Kelamin, INDONESIA, Tahun 2020</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-tabel2020tabledataset5-avrl06.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "</table>"
    st.markdown(table_html, unsafe_allow_html=True)