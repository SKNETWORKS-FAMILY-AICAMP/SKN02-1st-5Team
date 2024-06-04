import streamlit as st
<<<<<<< HEAD
from PIL import Image
import car_register as a

def run_home() :
    #st.subheader('홈 화면입니다')
    #st.text('대기화면')
    img = Image.open('./image.png')
    st.image(img)
    a.car_registration_crawl()


    
=======

def run_home() :
    st.subheader('홈 화면입니다')
    st.text('대기화면')
>>>>>>> 72f625b820518adb36922acb6ad4e4c8e3a7e506
