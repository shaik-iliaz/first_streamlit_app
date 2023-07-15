import streamlit

streamlit.title('my parent healthy diner')

streamlit.header('breakfast favorites')
streamlit.text('🥣Omega 3 & oatmeal')
streamlit.text('🥗kale, spinach&smothie')
streamlit.text('🐔Hard-boiled free-range egg')
streamlit.text('🥑🍞avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

