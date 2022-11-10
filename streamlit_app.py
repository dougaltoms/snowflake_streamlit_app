import streamlit as st
import pandas as pd

st.title('Test Application Menu')

#--------------------------#
st.header('Breakfast')
st.text('🥣 Blueberry Oatmeal')
st.text('🥞 Bacon panckaes')
st.text('🥓 Full English')

#--------------------------#
st.header('Build-Your-Own Smoothie')

# Get fruit list from S3 bucket and add multiselect
fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index("Fruit")
st.multiselect("Pick your fruits: ", list(fruit_list.index))
st.dataframe(fruit_list)
