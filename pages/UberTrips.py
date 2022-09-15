import streamlit as st
import matplotlib.pyplot as plt
from bokeh.plotting import figure
import plotly.figure_factory as ff
import numpy as np
import pandas as pd
import seaborn as sns

# import the data
data = pd.read_csv('uber-raw-data-apr14.csv' , sep=',')

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

st.sidebar.write('**UBER LAB3 - LOUIS ARBEY**')
color = st.sidebar.selectbox('Choose the color of the title', ('Lightblue 🟦', 'Green 🟩', 'Red 🟥', 'White ⬜', 'Yellow 🟨', 'Black ⬛'))
color = color.split(' ')[0]
st.markdown(f'<p style="font-family:Montserrat,sans-serif  ; color:{color}; font-size: 40px;">🚕 Uber data - April 14 🚕</p>', unsafe_allow_html=True)

st.write('**This is a demo of streamlit, using the Uber data from April 14, 2014.**')
st.markdown('*Data source: `uber-raw-data-apr14.csv`*')
st.write('---')

# describre main infos of the data set
st.write('**Main infos of the data set:**')
st.write(data.describe())
st.code("""
st.write(data.describe())
""", language='python')
st.write('---')


# Convert the date column to datetime
data["Date/Time"] = pd.to_datetime(data["Date/Time"])

# Add columns for the weekday, hour, and month
def get_dom(data):
    return data.day
data['dom'] = data['Date/Time'].map(get_dom)
def get_weekday(data):
    return data.weekday()
data['weekday'] = data['Date/Time'].map(get_weekday)
def get_hour(data):
    return data.hour
data['hour'] = data['Date/Time'].map(get_hour)
def get_day(data):
    return data.day
data['day'] = data['Date/Time'].map(get_day)

# We show first rows of the data
st.write('**First rows of the data:**')
st.write(data.head())
st.code("""
st.write(data.head())
""", language='python')
st.write('---')

# Frequency per day of the month
st.write('**Frequency per day of the month**')
st.bar_chart(data.dom.value_counts().sort_index())
st.code("""
st.bar_chart(data.dom.value_counts().sort_index())
""", language='python')
st.write('')
st.area_chart(data.dom.value_counts().sort_index())
st.code("""
st.area_chart(data.dom.value_counts().sort_index())
""", language='python')
st.write('---')

# Frequency per hour of the day
st.write('**Frequency per hour of the day**')
st.bar_chart(data.hour.value_counts().sort_index())
st.code("""
st.bar_chart(data.hour.value_counts().sort_index())
""", language='python')
st.write('')

# Frequency per weekday
st.write('**Frequency per weekday**')
data.weekday = data.weekday.map({0:'0Mon', 1:'1Tue', 2:'2Wed', 3:'3Thu', 4:'4Fri', 5:'5Sat', 6:'6Sun'})
# create a bar chart and order the days of the week
st.bar_chart(data.weekday.value_counts().sort_index())
st.code("""
data.weekday = data.weekday.map({0:'0Mon', 1:'1Tue', 2:'2Wed', 3:'3Thu', 4:'4Fri', 5:'5Sat', 6:'6Sun'})
st.bar_chart(data.weekday.value_counts().sort_index())
""", language='python')
st.write('---')

# Number of rides in a month per location
st.write('**Number of rides in a month per location**')
data_map = data[['Lat', 'Lon']]
data_map['latitude'] = data_map['Lat']
data_map['longitude'] = data_map['Lon']
st.map(data_map)
st.code("""
st.map(data_map)
# Data map is a dataframe with only the latitude and longitude
""", language='python')
st.write('---')


st.write('**Heatmap of hour by weekday with seaborn**')
st.set_option('deprecation.showPyplotGlobalUse', False)
data_heatmap = data.pivot_table(index='hour', columns='weekday', values='Lat', aggfunc='count')
sns.heatmap(data_heatmap)
st.pyplot()
st.write('---')