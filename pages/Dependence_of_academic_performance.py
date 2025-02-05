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

if __name__ == "__main__":
    col1, col2 = st.columns(2)
    defaultHeight= 370
    with col1:
        figStrip = px.strip(data, x=xColumn, y=finalAssessmentPropName,
                    labels={xColumn: '', finalAssessmentPropName: ''}, height = defaultHeight)
        st.plotly_chart(figStrip, use_container_width=True)

        figBox = px.box(data, x=xColumn, y=finalAssessmentPropName,
                    labels={xColumn: '', finalAssessmentPropName: ''}, height = defaultHeight)
        figBox.update_layout(xaxis_showticklabels=False, yaxis_showticklabels=False) 
        st.plotly_chart(figBox, use_container_width=True)

    with col2:
        average_data = data.groupby(xColumn)[finalAssessmentPropName].mean().reset_index()
        figMean = px.bar(average_data,
                     x=xColumn,
                     y=finalAssessmentPropName,
                     labels={xColumn: '', finalAssessmentPropName: ''}, height = defaultHeight)
        figMean.update_traces(marker=dict(line=dict(width=0)))
        st.plotly_chart(figMean, use_container_width=True)

        figPie = px.pie(data, values='G3', names=xColumn,
                         labels={xColumn: '', 'average': ''}, height=defaultHeight)
        st.plotly_chart(figPie, use_container_width=True)