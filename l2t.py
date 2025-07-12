import pandas as pd
import streamlit as st

l2t = pd.read_csv('/mnt/d/kivi_securities/l2t_df.csv')

#l2t

grouped_l2t = l2t[(l2t['STRATEGY'].str.contains('BaLTE')) & (~l2t['STRATEGY'].str.contains('rodman|curry'))].groupby('STRATEGY').count().sort_values(by='QUANTITY').reset_index()

grouped_l2t[['STRATEGY', 'QUANTITY']]

with st.sidebar:
    selected_strat = st.radio(
        'Select Strategy',
        grouped_l2t['STRATEGY']
    )

l2t[(l2t['STRATEGY'].str.contains(selected_strat)) & (~l2t['STRATEGY'].str.contains('rodman|curry'))]
