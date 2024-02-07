import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Listado de Juegos de mesa')
boardgames_data = pd.read_csv('./datasets/boardgames_ranks.csv')