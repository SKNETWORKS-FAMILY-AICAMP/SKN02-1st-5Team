import streamlit as st
from PIL import Image

def run_ERD() :
    #st.subheader('홈 화면입니다')
    #st.text('대기화면')
    img = Image.open('./ERD.png')
    st.image(img)