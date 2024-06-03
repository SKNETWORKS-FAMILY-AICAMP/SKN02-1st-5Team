import crawler
import pandas as pd
import streamlit as st
import plotly.express as px

def show_streamit(df):
    # 제목 설정
    st.title("자동차 정비 관련 정보")

    # 선택할 항목 리스트 생성
    ar = []
    for i in ['휘발유', '경유', '하이브리드', '전기']:
        for j in ['', '증감률', '부적합 증감률', '부적합']:
            ar.append(i + ' ' + j)
    while True:

        # 첫 번째 그래프 입력 받기

        # 두 번째 그래프 입력 받기
        #input2 = input1 + " " + "증감률"

        # 두 개의 입력값이 있는 경우
        input1=  st.text_input("첫 번째 그래프 항목을 선택하세요 ({} 중에서)".format(', '.join(ar)))
        fig = px.line(df, x='연도', y= input1, markers=True)
        st.plotly_chart(fig)
