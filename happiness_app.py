import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")
X_axis = st.selectbox("Select Data For the X-axis: ", ("gdp", "happiness"))
y_axis = st.selectbox("Select Data For the y-axis: ", ("gdp", "happiness"))

st.subheader(f"{X_axis} and {y_axis}")


def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


def get_data_anil(X, y):
    data = pd.read_csv("happy.csv")
    X_line = data[f"{X}"]
    y_line = data[f"{y}"]
    return X_line, y_line


X, y = get_data_anil(X_axis, y_axis)
figure = px.scatter(x=X, y=y, labels={"x": X_axis, "y": y_axis})
st.plotly_chart(figure)
