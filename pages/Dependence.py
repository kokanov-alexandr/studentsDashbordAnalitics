import sys
sys.path.append("..")
from index import loadData
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Анализ зависимостей")
data = loadData()

dependencies = {
    'Время в пути - Оценки': ('traveltime', 'Время в пути'),
    'Время на учёбу - Оценки': ('studytime', 'Время на учёбу'),
    'Пропуски - Оценки': ('absences', 'Количество пропусков'),
    'Свободное время - Оценки': ('freetime', 'Свободное время'),
    'Наличие отношений - Оценки': ('romantic', 'Наличие отношений'),
    'Употребеление алкоголя в бедние дни - Оценки': ('Dalc', 'Употребеление алкоголя в бедние дни'),
    'Употребеление алкоголя в выходные дни - Оценки': ('Walc', 'Употребеление алкоголя в выходные дни'),
    'Образование родителей - Оценки': ('Pedu', 'Образование родителей')
}

finalAssessmentPropName = 'G3'
column_options = list(dependencies.keys())
selectedDelepdence = st.selectbox('Выберите зависимость:', column_options)

xColumn, xLabel = dependencies[selectedDelepdence]

figStrip = px.strip(data, x= xColumn, y=finalAssessmentPropName,
                labels={xColumn: xLabel, finalAssessmentPropName: 'Итоговая оценка'},
                title=f"Зависимость оценок")    
st.plotly_chart(figStrip)
