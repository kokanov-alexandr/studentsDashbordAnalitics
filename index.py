import streamlit as st
import pandas as pd
import plotly.express as px

fileName = 'student-por.csv'

@st.cache_resource
def load_data():
    dtypes = {
        'age': 'int8',
        'Medu': 'int8',
        'Fedu': 'int8',
        'traveltime': 'int8',
        'studytime': 'int8',
        'failures': 'int8',
        'famrel': 'int8',
        'freetime': 'int8',
        'goout': 'int8',
        'health': 'int8',
        'absences': 'int8',
        'school': 'category',
        'sex': 'category',
        'address': 'category',
        'famsize': 'category',
        'Pstatus': 'category',
        'guardian': 'category',
        'schoolsup': 'category',
        'famsup': 'category',
        'paid': 'category',
        'activities': 'category',
        'nursery': 'category',
        'higher': 'category',
        'internet': 'category',
        'romantic': 'category'
    }
    
    df = pd.read_csv(fileName, dtype=dtypes)
    return df



if __name__ == "__main__":
    st.title("Распределение данных")

    data = load_data()
    column_options = data.columns.tolist()
    selected_column = st.selectbox("Выберите поле для анализа:", column_options, index = 10)

    st.subheader("Столбчатая диаграмма")
    counts = data[selected_column].value_counts().sort_index()
    fig_bar = px.bar(x=counts.index, y=counts.values,
                labels={'x': selected_column, 'y': 'Количество'},
                title=f'Распределение {selected_column}')
    st.plotly_chart(fig_bar, use_container_width= False)

    st.subheader("Круговая диаграмма")
    counts = data[selected_column].value_counts().sort_index()
    fig_pie = px.pie(names=counts.index, values=counts.values,
                title=f'Распределение {selected_column}')
    st.plotly_chart(fig_pie)
