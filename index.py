import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Мой интерактивный дашборд",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get help': 'https://www.example.com/help',
        'Report a bug': 'https://www.example.com/bug',
         'About': 'Этот дашборд был создан для анализа данных'
    }
)

st.title("Распределение данных")

@st.cache_data
def load_data(filename):
    df = pd.read_csv(filename)
    return df

data = load_data('student-por.csv')

column_options = data.columns.tolist()
selected_column = st.selectbox("Выберите поле для анализа:", column_options, index = 10)

tabs = ["Столбчатая диаграмма", "Круговая диаграмма"]
selected_tab = st.radio("Выберите тип диаграммы:", tabs)

if selected_tab == "Столбчатая диаграмма":
    st.subheader("Распределение данных (Столбчатая диаграмма)")
    counts = data[selected_column].value_counts().sort_index()
    fig_bar = px.bar(x=counts.index, y=counts.values,
                labels={'x': selected_column, 'y': 'Количество'},
                title=f'Распределение {selected_column}')
    st.plotly_chart(fig_bar, use_container_width= False)

elif selected_tab == "Круговая диаграмма":
    st.subheader("Распределение данных (Круговая диаграмма)")
    counts = data[selected_column].value_counts().sort_index()
    fig_pie = px.pie(names=counts.index, values=counts.values,
                title=f'Распределение {selected_column}')
    st.plotly_chart(fig_pie)
