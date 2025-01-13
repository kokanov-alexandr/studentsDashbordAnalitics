import sys
sys.path.append("..")
from index import load_data
import streamlit as st
import pandas as pd

data = load_data()
st.header("Набор данных")

search_term = st.text_input("Поиск по данным:", "")

if search_term:
    search_term = search_term.lower()
    filtered_data = data[data.apply(lambda row: any(str(value).lower().find(search_term) != -1 for value in row.fillna('').astype(str) ), axis=1)]
else:
    filtered_data = data

st.dataframe(filtered_data, height = 600)
