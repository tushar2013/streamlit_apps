import streamlit as st
import pandas as pd

choice_list = 'up_r2_choices.csv'

df = pd.read_csv(choice_list)
#df

branch = st.sidebar.multiselect(
    "Select Branch:",
    options=df['branch'].unique(),
    default=['md radiodiagnosis'])

if branch:
    st.dataframe(df[df['branch'] == branch[0]])
else:
    st.code('please select at least one branch')
