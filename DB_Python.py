from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
from bs4 import BeautifulSoup
import pymysql
import streamlit as st
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def scrape_page(page_number):
    url = f"https://www.speedmate.com/customer/FAQ?categoryNm=&pageNo={page_number}"
    driver.get(url)
    time.sleep(2) 
    
    bs = BeautifulSoup(driver.page_source, 'lxml')
    li = bs.find_all('dl', {'class':'faq'})
    
    page_text = []
    for faq in li:
        page_text.append(faq.get_text(separator=',', strip=True))
    
    return page_text

def extract_db():

    all_text = []

    for page in range(1, 3):
        all_text.extend(scrape_page(page))

    arr = []
    for text in all_text:
        for j in text:
            arr.append(j)
    str1 = ''.join(arr)
    str2 = str1.split(',')
    arr2 = list(str2)

    cnt =0
    for i in arr2:
        #print(i,cnt)
        cnt+=1
    arr2.insert(73,'Q')

    ans_arr=[]

    for i in range(len(arr2)) :
        a=1
        temp_str =''
        if arr2[i] =='A':
            while a :
                if i+a >= len(arr2):
                    a =0
                    ans_arr.append(temp_str)
                    pass
                else :
                    if arr2[i+a] == 'Q':
                        a = 0
                        ans_arr.append(temp_str)
                    else :
                        temp_str +=arr2[i+a]
                        a+=1


    cnt = 0
    arr3 = []
    arr4 = []
    ind1 = 0
    ind2 = 0
    for i in range(len(arr2)-1):
        if arr2[i] == 'Q' and cnt == 0:
            cnt+=1
            ind1 = i+1
        elif arr2[i] == 'A':
            ind2 = i+1
            cnt=1
            arr3.append(arr2[ind1: i])
        elif arr2[i] == 'Q' and cnt > 0:
            arr4.append(arr2[ind2: i])
            ind1 = i+1

    category= []
    question = []
    for j in range(len(arr3)) :
        category.append(arr3[j][0])
        question.append(arr3[j][1])

    # 드라이버 종료
    

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='car2', charset='utf8')
    cur = conn.cursor()

    # query = "INSERT INTO car2.faq2 (category, question, answer) VALUES ("
    # for i in range(len(category)):
    #     cur.execute(query + "'" + category[i] + "','"  +  question[i]+ "','"+ ans_arr[i]+"')")
    # conn.commit()

    # 연결 종료

    arr_1 = []
    cur.execute("SELECT * FROM faq3")
    print("index    category    question    answer")
    print("----------------------------------------------------")
    while (True) :
        temp = []
        row = cur.fetchone()
        if row== None :
            break
        data1 = (row[0] - 27778)
        data2 = row[1]
        data3 = row[2]
        data4 = row[3]
        temp.append(data1)
        temp.append(data2)
        temp.append(data3)
        temp.append(data4)
        arr_1.append(temp)
        # conn.commit()

    #conn.close()
    #driver.quit()
    df = pd.DataFrame(data = arr_1)
    st.dataframe(df)