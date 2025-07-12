import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

data = {
    'Name': ['Baba', 'Maa', 'Jaana', 'Meghna', 'Deeksha', 'Aavya',],
    'Group': ['Family', 'Family', 'Family', 'Friend', 'Friend', 'Bhanji',],
    'Location': ['MyHeart', 'MyHeart', 'MyHeart', 'Lucknow', 'Lucknow', 'Lucknow',],
}

df = pd.DataFrame(data)

with st.sidebar:
    selected_group = st.radio('GROUP', df.groupby('Group').count().reset_index())

df[(df['Group'].str.contains(selected_group, na=False))]
