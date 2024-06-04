import pandas as pd
import streamlit as st
import plotly.express as px
import requests
import crawler
<<<<<<< HEAD
import maintenance_stream
import home
import DB_Python
import ERD 
if __name__ == "__main__":
    st.title('SKN02-1st-5Team')
    tab1,tab2, tab3, tab4= st.tabs(["자동차 등록 대수", "자동차 정비 현황", 'FAQ', "ERD"])
=======
import show_stream
import home
if __name__ == "__main__":
    st.title('SKN02-1st-5Team')
    tab1,tab2, tab3, tab4= st.tabs(["홈", "자동차 정비 현황", 'FAQ', "ERD"])
>>>>>>> 72f625b820518adb36922acb6ad4e4c8e3a7e506
    
    with tab1 :
        home.run_home()
    with tab2:
        data = pd.read_csv('20240603151251___.csv')
        df, ar =  crawler.crawl(data)
        try:
<<<<<<< HEAD
            maintenance_stream.show_streamit(df, ar)
        except ValueError as e:
            print(e)
    with tab3:
        DB_Python.extract_db()

    with tab4:
        ERD.run_ERD()
=======
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
>>>>>>> 72f625b820518adb36922acb6ad4e4c8e3a7e506
