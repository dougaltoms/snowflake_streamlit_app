import streamlit as st
import pandas as pd
import requests

st.title('Welcome to my Restaurant')

#--------------------------#
st.header('Breakfast')
st.text('🥣 Blueberry Oatmeal')
st.text('🥞 Bacon panckaes')
st.text('🥓 Full English')

#--------------------------#
st.header('🥤 Build-Your-Own Smoothie')

# Get fruit list from S3 bucket and add multiselect
fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index("Fruit")

selected = st.multiselect("Pick your fruits: ", list(fruit_list.index), ['Banana', 'Strawberries'])
to_display = fruit_list.loc[selected]

st.dataframe(to_display)

st.header('FruityVice Fruit Advice')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
