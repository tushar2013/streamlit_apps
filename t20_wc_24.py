import pandas as pd
import streamlit as st

matches = pd.read_csv('/mnt/d/coding_playground/datasets/matches.csv')
matches 


with st.sidebar:
    TEAMS = st.selectbox('TEAMS', sorted(matches['Team_1'].unique()))
    STAGES = st.selectbox('TEAMS', matches['Match_type'].unique())

matches[(matches['Team_1'] == TEAMS) & (matches['Match_type'] == STAGES)]
