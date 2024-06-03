import pandas as pd
import streamlit as st
import plotly.express as px
import requests
import crawler
import show_stream
if __name__ == "__main__":
    data = pd.read_csv('20240603151251___.csv')
    df =  crawler.crawl(data)
    show_stream.show_streamit(df)