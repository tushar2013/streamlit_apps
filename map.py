import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
         [
             ['New_Delhi', 'New_Delhi', 28.644800, 77.216721], 
             ['Chopta', 'Uttarakhand', 30.346434, 79.048386],
             ['Jaisalmer', 'Rajasthan', 26.9157, 70.9083],
         ],
             columns = ['city', 'state', 'lat', 'lon']
     )

df
st.map(df)
