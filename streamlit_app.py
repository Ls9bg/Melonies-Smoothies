# Import python packages
import streamlit as st
#streamlit.title('My parents New Healthy Diner')
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col,when_matched
import requests
import pandas as pd

# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
  """Choose the fruits you want in your custom Smoothie!
  """
)


name_on_order = st.text_input("Name on Smoothie")
st.write("The name on your smoothie will be", name_on_order)


cnx=st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'),col('SEARCH_ON'))

#st.dataframe(data=my_dataframe, use_container_width=True)
ingredients_list=st.multiselect(
    'Choose up to 5 ingredients:'
    ,my_dataframe
    ,max_selections=5
)


if ingredients_list:
    ingredients_string= ''
    for fruit_chosen in ingredients_list:
      ingredients_string +=fruit_chosen +' '
      search_on=pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
      st.write ('The search value for ',fruit_chosen,' is ' ,search_on,'.')
