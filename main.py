import pandas as pd
import streamlit as st
import plotly.express as px
import requests
import crawler
import show_stream
import home
if __name__ == "__main__":
    st.title('SKN02-1st-5Team')
    menu = ['Home', '자동자 정비 현황', 'FAQ 현황', 'ERD']
    choice = st.sidebar.selectbox('메뉴', menu)
    
    if choice == menu[0] :
        home.run_home()
    elif choice == menu[1]:
       
        data = pd.read_csv('20240603151251___.csv')
        df, ar =  crawler.crawl(data)
        try:
            show_stream.show_streamit(df, ar)
        except ValueError as e:
            print(e)