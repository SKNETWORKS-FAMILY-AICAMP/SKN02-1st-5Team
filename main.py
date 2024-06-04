import pandas as pd
import streamlit as st
import plotly.express as px
import requests
import crawler
import maintenance_stream
import home
import DB_Python
import ERD 
if __name__ == "__main__":
    st.title('SKN02-1st-5Team')
    tab1,tab2, tab3, tab4= st.tabs(["자동차 등록 대수", "자동차 정비 현황", 'FAQ', "ERD"])
    
    with tab1 :
        home.run_home()
    with tab2:
        data = pd.read_csv('20240603151251___.csv')
        df, ar =  crawler.crawl(data)
        try:
            maintenance_stream.show_streamit(df, ar)
        except ValueError as e:
            print(e)
    with tab3:
        DB_Python.extract_db()

    with tab4:
        ERD.run_ERD()
