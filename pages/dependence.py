import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np

st.title("Анализ зависимостей")

@st.cache_data
def load_data(filename):
    df = pd.read_csv(filename)
    return df

data = load_data('student-por.csv')

column_options = data.columns.tolist()
firstSelectedColumn = st.selectbox("Выберите ось x:", column_options, index = 1)
secondSelectedColumn = st.selectbox("Выберите ось y:", column_options, index = 2)


st.subheader("Распределение итоговой оценки по наличию отношений")
fig_strip = px.strip(data, x=firstSelectedColumn, y=secondSelectedColumn,
                labels={'romantic': 'Наличие отношений', 'G3': 'Итоговая оценка'},
                title="Распределение итоговых оценок по наличию отношений")
st.plotly_chart(fig_strip)

chart_data = pd.DataFrame(data, columns=["age", "G3", "sex"])

st.vega_lite_chart(
   data,
   {
       "mark": {"type": "circle", "tooltip": True},
       "encoding": {
           "x": {"field": "age", "type": "quantitative"},
           "y": {"field": "G3", "type": "quantitative"},
           "color": {"field": "freetime", "type": "nominal"}
       },
   },
   theme=None
)