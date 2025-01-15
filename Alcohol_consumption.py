import streamlit as st
import pandas as pd
import plotly.express as px

fileName = 'student-por.csv'

@st.cache_resource
def loadData():
    df = pd.read_csv(fileName)
    df['Pedu'] = df['Medu'] + df['Fedu']
    return df

data = loadData()        

def create_average_alcohol_chart(data, x_column):
    average_data = data.groupby(x_column).agg({'Dalc': 'mean', 'Walc': 'mean'}).reset_index()
    fig = px.bar(
        average_data,
        x=x_column,
        y=['Dalc', 'Walc'],
        barmode='group',
        title='Среднее употребление алкоголя по возрасту',
        labels={
            'value': 'Среднее употребление',
            'age': 'Возраст',
            'sex': 'Пол',
            'school': 'Школа',
            'higher': 'Высшее образование'
        },
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig.update_traces(marker=dict(line=dict(width=0)))
    fig.update_layout(
        bargap=0.1,
        legend_title_text='Алкоголь'
    )
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    st.title("Употребление алкоголя")
    st.write("**Dalc** - Употребление алкоголя в будние дни")
    st.write("**Walc** - Употребление алкоголя в выходные дни")

    tab1, tab2, tab3, tab4 = st.tabs(["Пол", "Возраст", "Желание получить высшее образование", "Итоговая оценка"])

    with tab1:
        create_average_alcohol_chart(data, 'sex')

    with tab2:
        create_average_alcohol_chart(data, 'age')

    with tab3:
        create_average_alcohol_chart(data, 'higher')

    with tab4:
        create_average_alcohol_chart(data, 'G3')


    