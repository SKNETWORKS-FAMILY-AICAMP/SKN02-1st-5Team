import streamlit as st
from PIL import Image
import car_register as a

def run_home() :
    #st.subheader('홈 화면입니다')
    #st.text('대기화면')
    img = Image.open('./image.png')
    st.image(img)
    a.car_registration_crawl()
