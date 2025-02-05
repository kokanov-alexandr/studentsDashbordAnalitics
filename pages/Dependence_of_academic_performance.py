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

filter_columns_mapping = {
        'Пол': 'sex',
        'Возраст': 'age',
        'Школа': 'school',
        'Адрес': 'address',
        'Размер семьи': 'famsize',
        'Статус совместного проживания родителей': 'Pstatus',
        'Образование матери': 'Medu',
        'Образование отца': 'Fedu',
        'Работа матери': 'Mjob',
        'Работа отца': 'Fjob',
        'Причина выбора школы': 'reason',
        'Опекун': 'guardian',
        'Время в пути до школы': 'traveltime',
        'Время обучения': 'studytime',
        'Количество неудач класса': 'failures',
        'Доп. образовательная поддержка': 'schoolsup',
        'Поддержка семейного образованя': 'famsup',
        'Дополнительные платные занятия': 'paid',
        'Внеклассные занятия': 'activities',
        'Посещал детский сад': 'nursery',
        'Желание получить высшее образование': 'higher',
        'Наличие интернета': 'internet',
        'Наличие романтических отношений': 'romantic',
        'Отношения в семье': 'famrel',
        'Свободное время': 'freetime',
        'Проведение времени с друзьями': 'goout',
        'Употребление алкоголя в будние дни': 'Dalc',
        'Употребление алкоголя в выходные дни': 'Walc',
        'Состояние здоровья': 'health',
        'Количество пропущенных занятий': 'absences'
}

finalAssessmentPropName = 'G3'
columnOptions = list(dependencies.keys())
selectedDelepdence = st.selectbox('Выберите зависимость:', columnOptions)
xColumn, xLabel = dependencies[selectedDelepdence]

if __name__ == "__main__":
    filter_columns_russian = list(filter_columns_mapping.keys())
    selected_filter_columns_russian = st.sidebar.multiselect(
        "Выберите столбцы для фильтрации:",
        options=filter_columns_russian
    )

    filter_columns = [filter_columns_mapping[col] for col in selected_filter_columns_russian]

    filters = {}
    for column in filter_columns:
        unique_values = data[column].unique().tolist()
        selected_values = st.sidebar.multiselect(
            "",
            options=unique_values,
            default=unique_values
        )
        filters[column] = selected_values

    filtered_data = data.copy()
    for column, selected_values in filters.items():
        filtered_data = filtered_data[filtered_data[column].isin(selected_values)]

    col1, col2 = st.columns(2)
    defaultHeight = 370
    with col1:
        figStrip = px.strip(filtered_data, x=xColumn, y=finalAssessmentPropName,
                            labels={xColumn: '', finalAssessmentPropName: ''}, height=defaultHeight)
        st.plotly_chart(figStrip, use_container_width=True)

        figBox = px.box(filtered_data, x=xColumn, y=finalAssessmentPropName,
                        labels={xColumn: '', finalAssessmentPropName: ''}, height=defaultHeight)
        figBox.update_layout(xaxis_showticklabels=False, yaxis_showticklabels=False)
        st.plotly_chart(figBox, use_container_width=True)

    with col2:
        average_data = filtered_data.groupby(xColumn)[finalAssessmentPropName].mean().reset_index()
        figMean = px.bar(average_data,
                         x=xColumn,
                         y=finalAssessmentPropName,
                         labels={xColumn: '', finalAssessmentPropName: ''}, height=defaultHeight)
        figMean.update_traces(marker=dict(line=dict(width=0)))
        st.plotly_chart(figMean, use_container_width=True)

        figPie = px.pie(filtered_data, values='G3', names=xColumn,
                            labels={xColumn: '', 'average': ''}, height=defaultHeight)
        st.plotly_chart(figPie, use_container_width=True)
