import pandas as pd
import streamlit as st

hall_of_fame = pd.read_csv('/mnt/d/coding_playground/datasets/icc_hall_of_fame/icc_hall_of_fame.csv')

hall_of_fame

#f'Below data_frame is hall_of_fame'
#
#with st.sidebar:
#    #countries = hall_of_fame.groupby('country').count().reset_index()['country']
#    countries = st.radio('COUNTRIES', hall_of_fame.groupby('country').count().reset_index())
#
#hall_of_fame[(hall_of_fame['country'].str.contains(countries, na=False))]
