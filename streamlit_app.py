import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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

# create fruit api function
def get_fruit_data(fruit):

    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit)
    fruityvice_normalised = pd.json_normalize(fruityvice_response.json())

    return fruityvice_normalised

st.header('Fruit Advice')

try:
    fruit_choice = st.text_input('What fruit would you like information about?')
  
    if not fruit_choice:
        st.error("Please select a fruit to get its info")

    else:
        fruityvice_normalised = get_fruit_data(fruit_choice)
        st.dataframe(fruityvice_normalised)

except URLError as e:
    st.error()
  
my_connection = snowflake.connector.connect(**st.secrets["snowflake"])
my_cursor = my_connection.cursor()
my_cursor.execute("SELECT * FROM FRUIT_LOAD_LIST")

data_rows = my_cursor.fetchall()
st.header("Fruit list contains:")
st.dataframe(data_rows)

# # Allow user to add fruit to the list
# add_fruit = st.text_input("What fruit would you like to add?")
# my_cursor.execute(f"INSERT INTO FRUIT_LOAD_LIST VALUES {add_fruit}")
