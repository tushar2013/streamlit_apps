import streamlit as st
import pandas as pd

my_things = {
    'to_do': ['AWS', 'ML', 'web_scraping', 'open_source'],
    'priority': ['High', 'High', 'Medium', 'Low'],
    'start_date': ['24/9', '24/9', '24/9', '24/9',],
}

my_things_df = pd.DataFrame(my_things)

my_things_df
