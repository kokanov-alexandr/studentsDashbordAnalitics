import streamlit as st
import pandas as pd
import plotly.express as px

fileName = 'student-por.csv'

@st.cache_resource
def loadData():
    df = pd.read_csv(fileName)
    return df


if __name__ == "__main__":
    st.title("Распределение данных")

    data = loadData()
    columnOptions = data.columns.tolist()
    selectedColumn = st.selectbox("Выберите поле для анализа:", columnOptions, index = 10)

    st.subheader("Столбчатая диаграмма")
    counts = data[selectedColumn].value_counts().sort_index()
    figBar = px.bar(x=counts.index, y=counts.values,
                labels={'x': selectedColumn, 'y': 'Количество'},
                title=f'Распределение {selectedColumn}')
    st.plotly_chart(figBar, use_container_width= False)

    st.subheader("Круговая диаграмма")
    counts = data[selectedColumn].value_counts().sort_index()
    figPie = px.pie(names=counts.index, values=counts.values,
                title=f'Распределение {selectedColumn}')
    st.plotly_chart(figPie, theme='streamlit') 