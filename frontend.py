import streamlit as st
import pandas as pd
import requests


st.title("My Webscraping Form!")

data = None
city_name = None

with st.form("websraping_form"):

    search_term = st.text_input(label="What do you want to search for?")
    city = st.text_input(label="City Name")
    state = st.text_input(label="State Name")
    items = st.number_input(
        label="Number Of Results Wanted", step=1, min_value=8, max_value=100)

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(
            f"Scraping data for {items} {search_term} in {city}, {state}")
        city_name = city
        data = {
            "Search Term": search_term,
            "City": city,
            "State": state,
            "items": items
        }

        response = requests.post(
            "https://faafdaajalebii-krina-webscraping.hf.space/getResults", json=data)

        data = response.content

        df = pd.read_excel(data)

        st.dataframe(df)

if data:
    st.download_button(label="Download Excel File", data=data, file_name=f"{city_name} Consultancies Data.xlsx",
                       mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
