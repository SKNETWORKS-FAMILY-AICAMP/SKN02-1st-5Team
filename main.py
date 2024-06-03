import pandas as pd
import streamlit as st
import plotly.express as px
import requests
import crawler
import show_stream
import home
if __name__ == "__main__":
    st.title('SKN02-1st-5Team')
    tab1,tab2, tab3, tab4= st.tabs(["홈", "자동차 정비 현황", 'FAQ', "ERD"])
    
    with tab1 :
        home.run_home()
    with tab2:
        data = pd.read_csv('20240603151251___.csv')
        df, ar =  crawler.crawl(data)
        try:
            show_stream.show_streamit(df, ar)
        except ValueError as e:
            print(e)
    with tab3:
        pass
    with tab4:
        pass
    #elif choice == menu[3]:
    #    st.image(" ")
    #else:
    #    st.image(" ")