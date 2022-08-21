from PIL import Image
import streamlit as st
import pickle
import sys
from os import path

pickle_in = open(sys.path[1]+'\model.pkl','rb')
classifier = pickle.load(pickle_in)

def prediction(STATION,YEAR,MONTH,DAY,HOUR,PM10, PM2_5, NO2, O3, SO2, CO):  
    prediction = classifier.predict(
        [[STATION,YEAR,MONTH,DAY,HOUR,PM10, PM2_5, NO2, O3, SO2, CO]])
    print(prediction)
    return prediction

def getUserInput():
    stations = ['Prishtinë, IHMK', 'Prishtinë, Rilindja', 'Dardhishtë']
    stationChoice = st.sidebar.selectbox("Zgjedh Stacionin:",stations)
    if stationChoice == "Prishtinë, IHMK":
        station = 1
    elif stationChoice == "Prishtinë, Rilindja":
        station = 2
    elif stationChoice == "Dardhishtë":
        station = 3
    years = [2018, 2019, 2020, 2021]
    year = st.sidebar.selectbox("Viti:", years)
    month = st.sidebar.slider("Muaji", 1 ,12 ,5)
    day = st.sidebar.slider("Dita", 1, 31, 8)
    hour = st.sidebar.slider('Ora', 0, 23, 0)
    PM10 = st.sidebar.slider('PM10', 0.0, 1200.0, 13.2)
    PM2_5 = st.sidebar.slider('PM2_5', 0.0, 800.0, 5.5)
    NO2 = st.sidebar.slider('NO2', 0.0, 1000.0, 7.2)
    O3 = st.sidebar.slider('O3', 0.0, 800.0, 88.4)
    SO2 = st.sidebar.slider('SO2', 0.0, 1250.0, 5.5)
    CO = st.sidebar.slider('CO', 0.0, 11.0, 1.5)
    result = ""
    result = prediction(station, year, month, day, hour, PM10, PM2_5, NO2, O3, SO2, CO)
    if result == 0:
        image = Image.open(sys.path[1]+"\AA-00.png")
        st.image(image, caption='Cilësia e ajrit: E Mirë', use_column_width=True)
    elif result == 1:
        image = Image.open(sys.path[1]+"\AA-01.png")
        st.image(image, caption='Cilësia e ajrit: E pranueshme', use_column_width=True)
    elif result == 2:
        image = Image.open(sys.path[1]+"\AA-02.png")
        st.image(image, caption='Cilësia e ajrit: Mesatare', use_column_width=True)
    elif result == 3:
        image = Image.open(sys.path[1]+"\AA-03.png")
        st.image(image, caption='Cilësia e ajrit: E Dobët', use_column_width=True)
    elif result == 4:
        image = Image.open(sys.path[1]+"\AA-04.png")
        st.image(image, caption='Cilësia e ajrit: Shumë e Dobët', use_column_width=True)
    elif result == 5:
        image = Image.open(sys.path[1]+"\AA-05.png")
        st.image(image, caption='Cilësia e ajrit: Jashtzakonisht E Dobët')    

user_input = getUserInput()




