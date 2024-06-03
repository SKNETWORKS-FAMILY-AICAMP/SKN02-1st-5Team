import crawler
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import warnings

def show_streamit(df, ar):
    # 제목 설정
    warnings.filterwarnings('ignore')
    st.title("자동차 정비 관련 정보")
    ar2 = np.array(ar)
    input1=  st.text_input("첫 번째 그래프 항목을 선택하세요 ({} 중에서)".format(', '.join(ar2)), key = str(1))
    fig = px.line(df, x='연도', y= input1, markers=True)
    st.plotly_chart(fig)