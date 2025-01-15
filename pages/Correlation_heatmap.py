import sys
sys.path.append("..")
from index import loadData
import streamlit as st
import pandas as pd
import plotly.express as px

data = loadData()

st.subheader("Тепловая карта корреляций")

column_labels = {
    'G3': 'Оценка',
    'studytime': 'Время на учебу', 
    'absences': 'Кол-во пропусков',
    'freetime': 'Свободное время',
    'goout': 'Час-та прогулок',
    'health': 'Сост-ие здоровья',
    'famrel': 'Сем-ые отношения',
    'Dalc': 'Алк. в будни',
    'Walc': 'Алк. в вых.'
}

correlation_vars = list(column_labels.keys())
correlation_matrix = data[correlation_vars].corr()

fig_heatmap = px.imshow(
    correlation_matrix,
    labels=dict(color="Корреляция"),
    x=list(column_labels.values()),
    y=list(column_labels.values()),
    color_continuous_scale="RdBu",
    aspect="auto"
)

fig_heatmap.update_traces(text=correlation_matrix.round(2), texttemplate="%{text}")
fig_heatmap.update_layout(
    title="Корреляция между основными показателями",
    xaxis_title="",
    yaxis_title="",
    width=800,
    height=600
)

st.plotly_chart(fig_heatmap)

# Добавляем пояснение
st.markdown("""
    #### Значения корреляции:
    - От -1 до 1, где:
    - 1: сильная положительная корреляция
    - 0: нет корреляции - -1: сильная отрицательная корреляция""") 