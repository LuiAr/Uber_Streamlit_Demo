import streamlit as st
import matplotlib.pyplot as plt
from bokeh.plotting import figure
import plotly.figure_factory as ff
import numpy as np
import pandas as pd

# import the data
data = pd.read_csv("ny-trips-data.csv", delimiter = ',')

# better like this, no ?
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');

body {
    color: #fff;
    background-color: #000;
    text-align: center;
}   
</style>
    """, unsafe_allow_html=True)

st.sidebar.write('**NY trips LAB3 - LOUIS ARBEY**')
color = st.sidebar.selectbox('Choose the color of the title', ('Lightblue 🟦', 'Green 🟩', 'Red 🟥', 'White ⬜', 'Yellow 🟨', 'Black ⬛'))
color = color.split(' ')[0]
st.markdown(f'<p style="font-family:Montserrat,sans-serif  ; color:{color}; font-size: 40px;">🗽 NY data - 15 january 2015 🗽</p>', unsafe_allow_html=True)

st.write('**This is a demo of streamlit, using the NY trips data.**')
st.markdown('*Data source: `ny-trips-data.csv`*')
st.write('---')


# describre main infos of the data set
st.write('**Main infos of the data set:**')
st.write(data.describe())
st.code("""
st.write(data.describe())
""", language='python')
st.write('---')

# transform dates
data["tpep_pickup_datetime"] = pd.to_datetime(data["tpep_pickup_datetime"])
data["tpep_dropoff_datetime"] = pd.to_datetime(data["tpep_dropoff_datetime"])

# we show the first rows of the data
st.write('**First rows of the data:**')
st.write(data.head())
st.code("""
st.write(data.head())
""", language='python')
st.write('---')

def get_day(x):
    return x.day
def get_month(x):
    return x.month
def get_year(x):
    return x.year
def get_hour(x):
    return x.hour
def get_minute(x):
    return x.minute
def get_second(x):
    return x.second

# We first need to create a new column to get the hours of pickup.
data["hour"] = data["tpep_pickup_datetime"].apply(get_hour)
data["minute"] = data["tpep_pickup_datetime"].apply(get_minute)
data["second"] = data["tpep_pickup_datetime"].apply(get_second)
data["day"] = data["tpep_pickup_datetime"].apply(get_day)
data["month"] = data["tpep_pickup_datetime"].apply(get_month)
data["year"] = data["tpep_pickup_datetime"].apply(get_year)

# we show the 6 new columns
st.write('**We create columns for hours, days, etc...**')
dataNewCols = data[["hour", "minute", "second", "day", "month", "year"]]
st.write(dataNewCols.head())
st.write('---')

# We create a plot showing the average (mean) tip amount per hour of the day
st.write('**Average tip amount per hour of the day:**')
st.bar_chart(data.groupby("hour")["tip_amount"].mean())
data_container = st.container()
with data_container:
    table1, table2 = st.columns(2)
    with table1:
        st.write('Hours with the highest average tip amount')
        st.write(data.groupby("hour")["tip_amount"].mean().sort_values(ascending = False).head())
        st.code("""
        5h , 16h , 21h , 22h , 23h
        """, language='c')
    with table2:
        st.write('Hours with the lowest average tip amount')
        st.write(data.groupby("hour")["tip_amount"].mean().sort_values(ascending = True).head())
        st.code("""
        2h , 3h , 7h , 10h , 11h
        """, language='c')
st.write('---')


st.write("**Number of trips per hour of the day**")
st.bar_chart(data.groupby("hour")["tpep_pickup_datetime"].count())
st.write("We see that the number of trips goes down around midnight and rises again around 6am.")
st.write('---')



data_container2 = st.container()
with data_container2:
    table3, table4 = st.columns(2)
    with table3:
        st.write('**Pickup locations**')
        data["lat"] = data["pickup_latitude"]
        data["lon"] = data["pickup_longitude"]
        st.map(data[["lat", "lon"]])
    with table4:
        st.write('**Dropoff locations**')
        data["lat"] = data["dropoff_latitude"]
        data["lon"] = data["dropoff_longitude"]
        st.map(data[["lat", "lon"]])
st.write("Execpt one pickup at Youngstown, all the pickups are in New York.")

st.write('---')