import streamlit as st
import pandas as pd
import requests
import snowflake.connector

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

st.header('Fruit Advice')
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('You have entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
st.dataframe(fruityvice_normalized)

my_connection = snowflake.connector.connect(**st.secrets["snowflake"])
my_cursor = my_connection.cursor()
my_cursor.execute("SELECT * FROM FRUIT_LOAD_LIST")

data_rows = my_cursor.fetchall()
st.header("Fruit list contains:")
st.dataframe(data_rows)

# Allow user to add fruit to the list
add_fruit = st.text_input("What fruit would you like to add?")
