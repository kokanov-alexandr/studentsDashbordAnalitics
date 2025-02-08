import streamlit as st
import pandas as pd
import plotly.express as px

fileName = 'student-por.csv'

@st.cache_resource
def loadData():
    df = pd.read_csv(fileName)
    df['Pedu'] = df['Medu'] + df['Fedu']
    return df


def create_average_alcohol_chart(data, x_column):
    average_data = data.groupby(x_column).agg({'Dalc': 'mean', 'Walc': 'mean'}).reset_index()
    fig = px.bar(
        average_data,
        x=x_column,
        y=['Dalc', 'Walc'],
        barmode='group',
        labels={
            'value': '',
            'age': 'Возраст',
            'sex': 'Пол',
            'school': 'Школа',
            'higher': 'Желание иметь высшее образование',
            'G3': 'Итоговая оценка',
            'variable': 'Алкоголь'
        },
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig.update_traces(marker=dict(line=dict(width=0)))
    fig.update_layout(
        bargap=0.1,
        legend_orientation="h",
        legend_x=0.5,
        legend_y=1.15, 
        legend=dict(xanchor="center", yanchor="top"),
        height = 370
    )
    st.plotly_chart(fig, use_container_width=True)

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


if __name__ == "__main__":
    data = loadData()        
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
            f"Выберите значения для {column}:",
            options=unique_values,
            default=unique_values
        )
        filters[column] = selected_values

    filtered_data = data.copy()
    for column, selected_values in filters.items():
        filtered_data = filtered_data[filtered_data[column].isin(selected_values)]


    st.title("Употребление алкоголя")
    st.write("**Dalc** - Употребление алкоголя в будние дни")
    st.write("**Walc** - Употребление алкоголя в выходные дни")


    col1, col2 = st.columns(2)

    with col1:
        create_average_alcohol_chart(filtered_data, 'sex')
        create_average_alcohol_chart(filtered_data, 'age')

    with col2:
        create_average_alcohol_chart(filtered_data, 'higher')
        create_average_alcohol_chart(filtered_data, 'G3')




    