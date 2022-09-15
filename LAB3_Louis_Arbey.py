import streamlit as st
import matplotlib.pyplot as plt
from bokeh.plotting import figure
import plotly.figure_factory as ff
import numpy as np
import pandas as pd

st.markdown("""
<style>
body {
    color: #fff;
    background-color: #000;
    text-align: center;
}   
</style>
    """, unsafe_allow_html=True)

def main_page():
    st.markdown("# Select a dataset in the sidebar menu")

def UberTrips():
    st.sidebar.markdown("# Uber Trips 🚕")

def NyTrips():
    st.sidebar.markdown("# NY Trips 🗽")

page_names_to_funcs = {
    "Main Page": main_page,
    "Uber Trips 🚕": UberTrips,
    "NY Trips 🗽": NyTrips,
}

selected_page = st.sidebar.selectbox("Select a dataset", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


st.image('logo_efrei.png', width=500)

