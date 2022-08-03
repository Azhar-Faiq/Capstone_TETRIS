import streamlit as st

from PIL import Image

st.title("Dampak Dorongan Jokowi Pada Pertumbuhan Ekspor Indonesia")
st.markdown('---')

st.markdown("<div style='text-align: justify; color: black;'>Pada tahun 2020, Ditengah pandemi COVID-19 yang belum kunjung usai, Presiden Jokowi menginstruksikan untuk meningkatkan ekspor Indonesia. Walaupun volume perdagangan dunia sedang turun ekspor Indonesia tidak boleh pesimis dalam memanfaatkan kesempatan yang ada. Instruksi ini tidak hanya diperuntukan untuk perusahaan dan pemerintah tetapi juga kepada UKM. Dorongan kegiatan ekspor ditujukan untuk pemulihan ekonomi Indonesia.</div>", unsafe_allow_html=True)

st.subheader('Pertumbuhan ekspor dan dorongan jokowi di tengah pandemi')
#kolom untuk plot ekspor impor
kolom1,kolom2,kolom3 = st.columns([1,5,1])
with kolom1:
    st.write('')
with kolom2:
    plot_ekspor_impor=Image.open('plot_ekspor_impor.png')
    st.image(plot_ekspor_impor, caption="Perkembangan ekspor impor 2014-2022*Data 2021 hanya sampai bulan Mei")
with kolom3:
    st.write('')
kolom_metric_1,kolom_metric_2 = st.columns([1,1])
with kolom_metric_1 :
    tab1, tab2= st.tabs(["2019-2020", "2020-2021"])
    with tab1:
        st.metric('Pertumbuhan nilai ekspor 2019-2020','1.631T USD','-2.678%')

    with tab2:
        st.metric('Pertumbuhan nilai ekspor 2020-2021','2.316T USD','41.925%')

st.markdown(
    "<div style='text-align: justify; color: black;'>Berdasarkan rekam jejak nilai ekspor Indonesia sebelum pandemi, terlihat bahwa nilai ekspor Indonesia tidak terlalu menjanjikan. Beberapa tahun belakangan nilai ekpsor Indonesia sempat berada dibawah nilai impor. Datangnya pandemi di awal tahun 2020 dapat mengakibatkan semakin terpuruknya nilai ekspor indonesia. Namun justru kebalikanya yang terjadi.</div>", unsafe_allow_html=True)
st.write('')
st.markdown(
    "<div style='text-align: justify; color: black;'>Walaupun turun sebanyak 2,678%, nilai ekspor Indonesia masih berada di atas nilai impor Indonesia. Presiden Jokowi juga memanfaatkan kesempatan ini untuk mendorong kegiatan ekspor. Alhasil di akhir tahun 2020 selisih nilai antara ekspor dan impor naik sebesar 701%. Peningkatan besar ini mampu mengeluarkan Indonesia dari devisit pada tahun 2019</div>", unsafe_allow_html=True)
st.write('')
st.markdown('Dari [Tempo.co : Bisnis](https://bisnis.tempo.co/read/1404052/jokowi-ajak-tingkatkan-ekspor-banyak-eksekusi-jangan-hanya-rencana)')
st.markdown('>"Saya mengajak kita semua, eksportir, semua pejabat di Kementerian Perdagangan, para gubernur sampai dengan perwakilan Indonesia di luar negeri untuk bergerak lebih cepat, lebih solid dan  lebih terpadu. Lakukan lebih banyak eksekusi, jangan hanya rencana," kata Jokowi dalam pembukaan Trade Expo Indonesia Virtual Event, Selasa, 10 November 2020.')
st.write('')
st.markdown(
    "<div style='text-align: justify; color: black;'>Dilasir dari tempo bisnis, Jokowi mengajak berbagai elemen untuk meningkatkan kegiatan ekspor. Pak Jokowi juga menekankan untuk tidak hanya merencanakan tetapi juga eksekusi. Tidak hanya pengusaha besar dan pemerintah, UKM juga diajak untuk meningkatkan kualitas produk untuk diekspor. Tentu pengingkatan ekspor tidak naik hanya dalam waktu semalam. Selain ajakan tersebut banyak rencana yang dijalankan untuk meningkatkan ekspor indonseia. Hasil berbagai usaha yang telah dijalankan tercermin pada nilai ekspor di tahun 2021. Pada tahun tersebut nilai ekspor mencapai angka 2.316T USD. Nilai tersebut meningkat sebesar 41% dari nilai ekspor tahun sebelumnya.</div>", unsafe_allow_html=True)
        
    
with kolom_metric_2:
    tab1, tab2= st.tabs(["2019-2020", "2020-2021"])
    with tab1:
        st.metric('Pertumbuhan selisih nilai ekspor-impor 2019-2020','216M USD','701.853%')

    with tab2:
        st.metric('Pertumbuhan selisih nilai ekspor-impor 2020-2021','354M USD','63.804%')


st.subheader("Faktor pendorong ekspor Indonesia")
st.markdown(
    "<h4 style='text-align: justify; color: black;'>Hilirisasi industri komoditas ekspor</h4>", unsafe_allow_html=True)
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["2014", "2015","2016","2017","2018","2019",'2020','2021','2022'])
with tab1:
    st.header("2014")
    plot2= Image.open('persentase nilai ekspor 2014.png')
    st.image(plot2,caption="Persebaran komoditas ekspor 2014")

with tab2:
    st.header("2015")
    plot = Image.open('persentase nilai ekspor 2015.png')
    st.image(plot,caption="Persebaran komoditas ekspor 2015")

with tab3:
    st.header("2016")
    plot2= Image.open('persentase nilai ekspor 2016.png')
    st.image(plot2,caption="Persebaran komoditas ekspor 2016")

with tab4:
    st.header("2017")
    plot = Image.open('persentase nilai ekspor 2017.png')
    st.image(plot,caption="Persebaran komoditas ekspor 2017")

with tab5:
    st.header("2018")
    plot2= Image.open('persentase nilai ekspor 2018.png')
    st.image(plot2,caption="Persebaran komoditas ekspor 2018")

with tab6:
    st.header("2019")
    plot = Image.open('persentase nilai ekspor 2019.png')
    st.image(plot,caption="Persebaran komoditas ekspor 2019")

with tab7:
    st.header("2020")
    plot2= Image.open('persentase nilai ekspor 2020.png')
    st.image(plot2,caption="Persebaran komoditas ekspor 2002")

with tab8:
    st.header("2021")
    plot = Image.open('persentase nilai ekspor 2021.png')
    st.image(plot,caption="Persebaran komoditas ekspor 2021")

with tab9:
    st.header("2022")
    plot2= Image.open('persentase nilai ekspor 2022.png')
    st.image(plot2,caption="Persebaran komoditas ekspor 2022 *sampai mei 2022")


st.markdown(
    "<div style='text-align: justify; color: black;'>Peningkatan nilai ekspor indonesia dimungkinkan dengan adanya fokus pada hilirisasi komoditas ekspor. Walaupun nilai ekspor sebagian besar tetap dikontribusi oleh bahan bakar mineral dan berbagai minyak hewani dan nabati. Pergeseran komoditas akibat hilirisai terlihat pada komoditas besi dan baja yang mulai meningkat sejak tahun 2020. Kenaikan tersebut cukup signifikan hingga menjadikan Besi dan baja menjadi komoditas ketiga yang penyumbang nilai ekspor terbanyak di tahun 2021.</div>", unsafe_allow_html=True)
st.write('')
st.markdown(
    "<div style='text-align: justify; color: black;'>Perubahan komoditas ini diharapkan dapat menejalar ke komoditas barang setengah jadi dan barang jadi lainya. Sudah seharusnya Indonesia memiliki target untuk bisa mengolah berbagai bahan mentah menjadi barang jadi.</div>", unsafe_allow_html=True)

st.markdown(
    "<h4 style='text-align: justify; color: black;'>Pembangunan infrastruktur perdagangan maritim</h4>", unsafe_allow_html=True)
st.markdown('Dari [Media Indonesia](https://mediaindonesia.com/ekonomi/279312/tol-laut-dongkrak-pertumbuhan-ekspor-di-sulsel)')
st.markdown('>"Ini berkat kehadiran Makassar New Port (MNP) yang mendukung direct export dan direct call, khususnya dari Makassar. Yang pada awalnya hanya melayani pengiriman barang 40 kontainer, kini menjafi 100 ribu TEUs kontainer, dengat traffic per bulan 10 ribu TEUs," ungkap Direktur Utama PT Pelindo IV Fardi Padang, Sabtu, (21/12/2019).')
st.write('')
st.markdown(
    "<div style='text-align: justify; color: black;'>Pembangunan infrastruktur perdagangan maritim juga turun mendunkung kegiatan ekspor Indonesia. Pembangunan berbagai pelabuhan baru membuat kegiatan ekspor dapat dilakukan di berbagai titik. Salah satunya adanya pelabuhan Makassar New Port. Pembangunan Makassar New Port sudah dilakukan sejak tahun 2015 dan saat sudah mencapai 84,41%. Direncakanan pelabuhan MNP dapat menampung 2.5 juta TEUs peti kemas. </div>", unsafe_allow_html=True)
st.write('')
st.markdown(
    "<div style='text-align: justify; color: black;'>Pelabuhan lainya yang dicanangkan akan mendukung kegiatan ekspor terutama ekspor kendaraan bermotor adalah pelabuhan patimban. Pelabuhan ini sudah mulai beroperasi sejak tahun 2020. Pada peresmiannya pelabuhan ini langsung digunakan untuk mengekspor kendaraan beroda empat ke Brunei Darussalam </div>", unsafe_allow_html=True)
st.write('')
st.markdown(
    "<div style='text-align: justify; color: black;'>Selain pembangunan pelabuhan, program tol laut juga ikut mendungkung kegiatan ekspor. Per tahun 2021 tol laut sudah memiliki 32 trayek, 32 kapal, dan 114 pelabuhan. Program tol laut ini ditujukan untuk mendukung logistik terutama di daerah 3T. Persebaran logistik yang semakin merata mendukung untuk dilakukannya ekspor. Karena program ini juga MNP mampu memiliki kemampuan direct ekspor ke berbagai negara. </div>", unsafe_allow_html=True)

st.markdown(
    "<h3 style='text-align: justify; color: black;'>Referensi:</h3>", unsafe_allow_html=True)
st.markdown('[BTKI 2022, Beacukai](https://www.beacukai.go.id/arsip/lan/BTKI-2022.html)')
st.markdown('[Data ekspor impor, BPS](https://www.bps.go.id/exim/)')
st.markdown('[Jokowi Instruksikan Percepat Pembangunan Pelabuhan Terbesar di Indonesia, VOA Indonesia](https://www.voaindonesia.com/a/jokowi-instruksikan-percepat-pembangunan-pelabuhan-terbesar-di-indonesia/5593086.html)')
st.markdown('[Jokowi Ajak Tingkatkan Ekspor: Banyak Eksekusi, Jangan Hanya Rencana, Tempo.co](https://bisnis.tempo.co/read/1404052/jokowi-ajak-tingkatkan-ekspor-banyak-eksekusi-jangan-hanya-rencana)')
st.markdown('[Presiden Jokowi Optimis Ekspor Mobil akan Terus Naik, Pedoman Rakyat News.com](https://www.pedomanrakyatnews.com/nasional/pr-3352895972/presiden-jokowi-optimis-ekspor-mobil-akan-terus-naik)')
st.markdown('[Presiden Jokowi Optimistis Hilirisasi Industri Mampu Tingkatkan Nilai Tambah di Sektor Industri, Menpan](https://www.bps.go.id/exim/)')
st.markdown('[Tol Laut Dongkrak Pertumbuhan Ekspor di Sulsel, Media Indonesia ](https://mediaindonesia.com/ekonomi/279312/tol-laut-dongkrak-pertumbuhan-ekspor-di-sulsel)')
st.markdown('[Diresmikan Jokowi pada 2015, Ini Progres Proyek Makassar New Port, Bisnis.com](https://ekonomi.bisnis.com/read/20220119/98/1491022/diresmikan-jokowi-pada-2015-ini-progres-proyek-makassar-new-port)')
st.markdown('[Mulai Beroperasi, Pelabuhan Patimban Langsung Layani Ekspor Perdana, Dephub](http://dephub.go.id/post/read/mulai-beroperasi,-pelabuhan-patimban-langsung-layani-ekspor-perdana)')
st.markdown('[Masuk Usia 7 Tahun, Ini Capaian Program Tol Laut, BPS](https://ekonomi.bisnis.com/read/20211022/98/1456990/masuk-usia-7-tahun-ini-capaian-program-tol-laut)')