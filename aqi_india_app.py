import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

# Define reusable border style
box_style = """
    <div style="
        border: 2px solid blue;
        border-radius: 10px;
        padding: 20px;
        background-color: #f9f9f9;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        width: 500px;
        text-align: center;
        ">
        {content}
    </div>
"""

aqi_df = pd.read_csv('/home/neo/coding_playground/datasets/aqi_india.csv')
#aqi_df

state = st.sidebar.selectbox('States', aqi_df['state'].unique())

city = st.sidebar.selectbox(
           'Cities', 
           aqi_df[aqi_df['state'] == state]['city'].unique()
       ) # select distinct(city) from aqi_df where state=state

station = st.sidebar.selectbox(
           'Stations', 
           aqi_df[aqi_df['city'] == city]['station'].unique()
          ) # select distinct((station) from aqi_df where city=city

aqi_df[
    (aqi_df['state'] == state) & 
    (aqi_df['city'] == city) & 
    (aqi_df['station'] == station)
    ][[
        'last_update', 'pollutant_id', 
        'pollutant_min', 'pollutant_max',
        'pollutant_avg'
    ]]

sum, mean, min, max, count, first, last = st.columns(7)

#with sum:
if st.button('Sum'):
    grouped_data = aqi_df.groupby('state')['pollutant_max'].sum().reset_index()
    output = grouped_data[grouped_data['state'] == state]['pollutant_max'].values[0]
    st.markdown(box_style.format(content=f'Total max pollutant in {state.upper()} is {output}'), unsafe_allow_html=True)
    
#with mean:
else:
    if st.button('Mean'):
        grouped_data = aqi_df.groupby('state')['pollutant_max'].mean().reset_index()
        output = grouped_data[grouped_data['state'] == state]['pollutant_max'].values[0]
        st.markdown(box_style.format(content=f'Mean max pollutant in {state.upper()} is {output: .2f}'), unsafe_allow_html=True)

# Set default values in session state
if 'yes_clicked' not in st.session_state:
    st.session_state.yes_clicked = False

if 'no_clicked' not in st.session_state:
    st.session_state.no_clicked = False

# When yes button is clicked
if st.button('yes'):
    st.session_state.yes_clicked = True

# When no button is clicked
if st.button('no'):
    st.session_state.no_clicked = True

# Show results based on session state
if st.session_state.yes_clicked:
    st.write("✅ You clicked YES")

if st.session_state.no_clicked:
    st.write("❌ You clicked NO")

