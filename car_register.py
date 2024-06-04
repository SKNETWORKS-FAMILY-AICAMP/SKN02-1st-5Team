import plotly.express as px
import pandas as pd
import streamlit as st
def car_registration_crawl():
    data2 = pd.read_csv('./28e3d7f02d630f39.csv',encoding='CP949')
    data2.dropna(inplace=True)

    select_columns = [	'Unnamed: 0','Unnamed: 1','Unnamed: 2' ,'Unnamed: 3']

    re_df = data2[select_columns]

    re_df.rename(columns = {'Unnamed: 0' : 'year','Unnamed: 1' : 'amount', 'Unnamed: 2' : 'increase' , 'Unnamed: 3':'Irate'}, inplace = True)



    data2_n_0=re_df['year'].astype(int)
    data2_n_1=re_df['amount'].astype(int)
    data2_n_2=re_df['increase'].astype(int)
    data2_n_3=re_df['Irate'].astype(float)

    df4 = pd.concat([data2_n_0,data2_n_1,data2_n_2,data2_n_3],axis =1)
    df4.set_index("year",inplace = True)
   

    fig = px.line(df4['amount'], markers=True)
    st.plotly_chart(fig)