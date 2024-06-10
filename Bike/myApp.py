import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from PyPDF2 import PdfReader
import io
import os
import matplotlib.pyplot as plt
import docx2txt
from pdf2image import convert_from_path
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title = "Bikers",
    page_icon = ":racing_motorcycle:",
    initial_sidebar_state = "expanded"
)

image_path = "Bike/cache.png"

@st.cache_resource
def load_image(image_file):
    img = Image.open(image_file)
    return img


def read_pdf_2(file_path):
    images = convert_from_path(file_path)
    return images




menu = ["Ana Sayfa","Hakkında", "Makale & Blog", "Ürün İncelemeleri", "Forum & Tartışma", "Topluluk", "Önce Güvenlik!", "Etkinlik Takvimi", "Yol Hali", "Aramıza Katılın"]
choice = st.sidebar.selectbox("Menü", menu)
cacha_image = st.sidebar.image("Bike/cache.png", caption='"Özgürlüğe Giden Yol!"')

if choice == ("Ana Sayfa"):
    st.title("RÜZGÂRIN RUHU")
    st.subheader('"İki teker üzerinde dünya daha büyük görünür."')
    st.write("""
    
    """)
if choice == ("Hakkında"):
    st.title("Motorcular için Buluşma Noktası")
    st.subheader('Özgürlüğe Giden Yol')

    st.write("""
    Aramıza hoş geldin!
Bu web sitesi, motosiklet tutkunlarının bir araya geldiği, deneyimlerini paylaştığı ve motosikletlerle ilgili her türlü bilgiye ulaşabileceği bir platformdur. 
Burada motor bakımı, sürüş teknikleri, motosiklet ekipmanları ve daha birçok konuda bilgi edinebilirsiniz. 
Yolculuk hikayelerinizi paylaşabilir, diğer motorcularla tanışabilir ve topluluğumuzun bir parçası olabilirsiniz.
Ve en güzeli, platform üyeleriyle buluşup turlara katılabilir, yeni maceralara atılabilir ve hayatın bambaşka bir yönüyle tanışabilirsin.

### Neler Bulabilirsiniz?
- **Makale ve Blog Yazıları:** Motosikletlerle ilgili en son haberler ve ipuçları.
- **Forum ve Tartışma:** Diğer motorcularla bilgi alışverişinde bulunma.
- **Etkinlikler ve Buluşmalar:** Motosiklet buluşmaları ve etkinlikleri hakkında bilgi.
- **Ürün İncelemeleri:** En yeni motosiklet ekipmanları ve aksesuarları hakkında incelemeler.

### Bize Katılın!
Motosiklet dünyasının bir parçası olun ve özgürlüğe giden yolda bize katılın!


    """)

if choice == ("Makale & Blog"):
    st.title("İki Teker Üzerindeki Hayat")


    #Makale&Blog ekle
    def on_button_click():
        uploaded_file = st.file_uploader("Dosya seç", type=['txt', 'pdf', 'csv'])
        if uploaded_file is not None:
            st.write("Dosya yüklendi!")

    # Butonu ekle
    if st.button('Paylaş'):
        on_button_click()






    st.write("""
             """)

if choice == ("Önce Güvenlik!"):
    st.title("Hızlı ve Güvenli")
    st.subheader("Kaosun Göbeğinde Yaşama Şansınızı Nasıl Yükseltirsiniz?")
    st.write('''
    
Motosiklet kazalarında kask kullanımı, sürücülerin hayatta kalma oranlarını önemli ölçüde etkiler. İşte kasklı ve kasksız sürücülerin kaza sonrası hayatta kalma oranlarına ilişkin bazı veriler:

Amerikan Ulusal Karayolu Trafik Güvenliği İdaresi (NHTSA):

Kask takan motosiklet sürücüleri, ölümcül kaza geçirme riskini yaklaşık %37 oranında azaltmaktadır.
Yolcular için bu oran %41'dir.
NHTSA'nın 2017 raporuna göre, kask takmak yaklaşık 1.872 kişinin hayatını kurtarmıştır ve kask takmayan 749 kişinin ölümleri önlenebilirdi .
 '''
)
    # NHTSA oranlarına göre kask kullanımı
    data = {
        'Kask Kullanımı': ['Kask Kullanan Sürücüler', 'Kask Kullanmayan Sürücüler'],
        'Değer': [0.41, 0.59]
    }
    colors = ["blue", "red"]
    # Plotly ile pie chart oluşturma
    fig = px.pie(data, values='Değer', names='Kask Kullanımı', title='Kaza Sonucu Hayatta Kalma Oranları', color_discrete_sequence=colors)

    # Streamlit ile grafiği gösterme

    st.plotly_chart(fig)

    st.write('''
Centers for Disease Control and Prevention (CDC):

CDC, kask kullanımının motosiklet kazalarında ölüm riskini %37 oranında azalttığını ve ciddi yaralanmaları %69 oranında azalttığını bildirmektedir .
''')
# CDC oranlarına göre kask kullanımı
    data = {
        'Kask Kullanımı': ['Kask Kullanan Sürücüler', 'Kask Kullanmayan Sürücüler'],
        'Değer': [0.37, 0.69]
    }
    colors = ["yellow", "black"]
    # Plotly ile pie chart oluşturma
    fig = px.pie(data, values='Değer', names='Kask Kullanımı', title='Kaza Sonucu Hayatta Kalma Oranları', color_discrete_sequence=colors)

    # Streamlit ile grafiği gösterme

    st.plotly_chart(fig)

    st.write('''
Dünya Sağlık Örgütü (WHO):

WHO, kask takmanın motosiklet sürücülerinin ölüm riskini %42, ciddi yaralanma riskini ise %69 oranında azalttığını belirtmektedir .
Bu veriler, kask kullanımının motosiklet sürücülerinin kazalardan sağ çıkma oranını önemli ölçüde artırdığını ve ciddi yaralanmalara karşı koruma sağladığını açıkça göstermektedir.
  

''')
    # WHO oranlarına göre kask kullanımı
    data = {
        'Kask Kullanımı': ['Kask Kullanan Sürücüler', 'Kask Kullanmayan Sürücüler'],
        'Değer': [0.42, 0.58]
    }
    colors = ["green", "gray"]
    # Plotly ile pie chart oluşturma
    fig = px.pie(data, values='Değer', names='Kask Kullanımı', title='Kaza Sonucu Hayatta Kalma Oranları',
                 color_discrete_sequence=colors)

    # Streamlit ile grafiği gösterme

    st.plotly_chart(fig)

if choice == ("Etkinlik Takvimi"):
        st.title("Hızlı ve Güvenli")
    
        def on_button_click():
            uploaded_file = st.file_uploader("Dosya seç", type=['txt', 'pdf', 'csv'])
            if uploaded_file is not None:
                st.write("Dosya yüklendi!")

            #  etkinlik Butonu ekle

            # Etkinlik oluştur butonu
                if st.button("Etkinlik Oluştur"):
                    event_date = st.date_input("Etkinlik Tarihi", date.today())
                    st.write("Seçilen etkinlik tarihi:", event_date)

                # Seçilen tarihe bağlı olarak açıklama metni
                    if event_date:
                        event_description_label = f"Açıklama ({event_date.strftime('%d.%m.%Y')})"
                        event_description = st.text_area(event_description_label)
                        st.write("Açıklama:", event_description)

                        if st.button("Oluştur"):
                            event_date = st.date_input("Etkinlik Tarihi", date.today())
                            st.write("Seçilen etkinlik tarihi:", event_date)





# python -m streamlit run myApp.py --server.runOnSave=True
