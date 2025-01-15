import sys
sys.path.append("..")
from Alcohol_consumption import loadData
import streamlit as st
import pandas as pd
import plotly.express as px

data = loadData()

def display_heatmap(columLabels, title):
    correlationVars = list(columLabels.keys())
    correlationMatrix = data[correlationVars].corr()
    fig = px.imshow(    
        correlationMatrix,
        labels=dict(color="Корреляция"),
        x=list(columLabels.values()),
        y=list(columLabels.values()),
        color_continuous_scale="RdBu",
        aspect="auto"
    )
    fig.update_traces(text=correlationMatrix.round(2), texttemplate="%{text}")
    fig.update_layout(
        title=title,
        xaxis_title="",
        yaxis_title="",
        width=800,
        height=600
    )
    st.plotly_chart(fig)

gColumLabels = {
    'G1': 'Оценка за 1-ый период',
    'G2': 'Оценка за 2-ой период',
    'G3': 'Итоговая оценка',
    'studytime': 'Время на учебу', 
    'absences': 'Кол-во пропусков',
    'goout': 'Час-та прогулок',
    'Pedu': 'Образование род-ей',
}

alcoColumLabels = {
    'studytime': 'Время на учебу', 
    'freetime': 'Свободное время',
    'goout': 'Час-та прогулок',
    'health': 'Сост-ие здоровья',
    'famrel': 'Сем-ые отношения',
    'Dalc': 'Алк. в будни',
    'Walc': 'Алк. в вых.',
}


st.title("Тепловые карты корреляций")
display_heatmap(gColumLabels, "Корреляция успеваемости с факторами обучения")
display_heatmap(alcoColumLabels, "Корреляция социальных факторов и употребления алкоголя")