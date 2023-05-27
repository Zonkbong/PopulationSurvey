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
    table_html += "     <td>Penduduk yang pindah menurut Wilayah dan Jenis Kelamin</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-chart2010chartdataset1-wgid20.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>2</td>\n"
    table_html += "     <td>Penduduk menurut Wilayah, Kelompok Umur, dan Jenis Kelamin</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-chart2010chartdataset2-zprhmv.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>3</td>\n"
    table_html += "     <td>Penduduk menurut Wilayah, Klasifikasi Generasi</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-chart2010chartdataset3-hoqotn.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>4</td>\n"
    table_html += "     <td>Penduduk Menurut  Kesesuaian Alamat KK dengan Domisili</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-chart2010chartdataset4-cneoog.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>5</td>\n"
    table_html += "     <td>Penduduk menurut Wilayah dan Jenis Kelamin</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-chart2010chartdataset5-3rijcf.streamlit.app/><button>Lihat Data</button></a></td>"
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
    table_html += "     <td>Penduduk yang pindah menurut Wilayah dan Jenis Kelamin</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-chart2020chartdataset1-8zwnqd.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>2</td>\n"
    table_html += "     <td>Jumlah Penduduk yang Pindah Menurut Wilayah dan Jenis Kelamin, INDONESIA, Tahun 2020</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-chart2020chartdataset2-ok2gr8.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>3</td>\n"
    table_html += "     <td>Penduduk menurut Wilayah, Klasifikasi Generasi</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-chart2020chartdataset3-j5nzcq.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>4</td>\n"
    table_html += "     <td>Penduduk Menurut  Kesesuaian Alamat KK dengan Domisili</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-chart2020chartdataset4-c639he.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "     <td>5</td>\n"
    table_html += "     <td>Jumlah Penduduk menurut Wilayah dan Jenis Kelamin, INDONESIA, Tahun 2020</td>\n"
    table_html += "     <td><a href=https://zonkbong-populationsurvey-chart2020chartdataset5-ynstdy.streamlit.app/><button>Lihat Data</button></a></td>"
    table_html += "  </tr>\n"

    table_html += "</table>"
    st.markdown(table_html, unsafe_allow_html=True)