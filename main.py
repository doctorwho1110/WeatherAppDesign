import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", max_value=5, min_value=1,
                 help="Select the number for forecasted days")
option = st.selectbox("Select data to review", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place} ")
