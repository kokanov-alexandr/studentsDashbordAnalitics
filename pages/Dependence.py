import sys
sys.path.append("..")
from Alcohol_consumption import loadData
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Зависимость успеваемости от внешних факторов")
data = loadData()

dependencies = {
    'Время в пути': ('traveltime', 'Время в пути'),
    'Время на учёбу': ('studytime', 'Время на учёбу'),
    'Пропуски': ('absences', 'Количество пропусков'),
    'Свободное время': ('freetime', 'Свободное время'),
    'Наличие отношений': ('romantic', 'Наличие отношений'),
    'Употребеление алкоголя в будние дни': ('Dalc', 'Употребеление алкоголя в будние дни'),
    'Употребеление алкоголя в выходные дни': ('Walc', 'Употребеление алкоголя в выходные дни'),
    'Образование родителей ': ('Pedu', 'Образование родителей')
}

finalAssessmentPropName = 'G3'
column_options = list(dependencies.keys())
selectedDelepdence = st.selectbox('Выберите зависимость:', column_options)

xColumn, xLabel = dependencies[selectedDelepdence]

figStrip = px.strip(data, x= xColumn, y=finalAssessmentPropName,
                labels={xColumn: xLabel, finalAssessmentPropName: 'Итоговая оценка'},
                title=f"Зависимость оценок")    
st.plotly_chart(figStrip)
figBox = px.box(data, x=xColumn, y=finalAssessmentPropName,
            labels={xColumn: xLabel, finalAssessmentPropName: 'Итоговая оценка'},
            title=f"Распределение оценок")
st.plotly_chart(figBox)
