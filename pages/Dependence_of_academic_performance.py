import sys
sys.path.append("..")
from Alcohol_consumption import loadData
import streamlit as st
import plotly.express as px

st.title("Зависимость успеваемости от внешних факторов")
data = loadData()

dependencies = {
    'Время на учёбу': ('studytime', 'Время на учёбу'),
    'Пол': ('sex', 'Пол'),
    'Свободное время': ('freetime', 'Свободное время'),
    'Употребеление алкоголя в будние дни': ('Dalc', 'Употребеление алкоголя в будние дни'),
    'Употребеление алкоголя в выходные дни': ('Walc', 'Употребеление алкоголя в выходные дни'),
    'Образование родителей ': ('Pedu', 'Образование родителей'),
    'Интернет': ('internet', 'Интернет'),   
    'Свободное время': ('freetime', 'Свободное время'),
    'Желание получить высшее образование': ('higher', 'Желание получить высшее образование'),
    'Дополнительные платные занятия': ('paid', 'Дополнительные платные занятия')
}

finalAssessmentPropName = 'G3'
columnOptions = list(dependencies.keys())
selectedDelepdence = st.selectbox('Выберите зависимость:', columnOptions)
xColumn, xLabel = dependencies[selectedDelepdence]

tab1, tab2, tab3 = st.tabs(["Точечная диаграмма", "Ящик с усами", "Средние значения"])

with tab1:
    figStrip = px.strip(data, x=xColumn, y=finalAssessmentPropName,
                    labels={xColumn: xLabel, finalAssessmentPropName: 'Итоговая оценка'},
                    title=f"Зависимость успеваемости")    
    st.plotly_chart(figStrip)

with tab2:
    figBox = px.box(data, x=xColumn, y=finalAssessmentPropName,
                labels={xColumn: xLabel, finalAssessmentPropName: 'Итоговая оценка'},
                title=f"Распределение успеваемости")
    st.plotly_chart(figBox)

with tab3:
    average_data = data.groupby(xColumn)[finalAssessmentPropName].mean().reset_index()
    figMean = px.bar(average_data, 
                     x=xColumn, 
                     y=finalAssessmentPropName,
                     labels={xColumn: xLabel, finalAssessmentPropName: 'Средняя итоговая оценка'},
                     title="Средние значения оценок")
    figMean.update_traces(marker=dict(line=dict(width=0)))
    st.plotly_chart(figMean)
