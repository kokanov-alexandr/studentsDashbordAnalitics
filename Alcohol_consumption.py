import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

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
        labels={
            'value': '',
            'age': 'Возраст',
            'sex': 'Пол',
            'school': 'Школа',
            'higher': 'Высшее образование',
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

if __name__ == "__main__":
    st.title("Употребление алкоголя")
    st.write("**Dalc** - Употребление алкоголя в будние дни")
    st.write("**Walc** - Употребление алкоголя в выходные дни")


    col1, col2 = st.columns(2)

    with col1:
        create_average_alcohol_chart(data, 'sex')
        create_average_alcohol_chart(data, 'age')

    with col2:
        create_average_alcohol_chart(data, 'higher')
        create_average_alcohol_chart(data, 'G3')




    