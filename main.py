import numpy as np
import pandas as pd

import streamlit as st


st.title('success_rate by operator')
df = pd.read_csv('Piece_Dimension.csv')
df['Volume'] =(df['Length'] *  df['Width'] *  df['Height']).astype(int)
df['Fault'] = [ 'normal' if 91134 < volume < 109242 else 'fault' for volume in df['Volume']]
fault_df = df[['Operator', 'Fault']]
normal_counts = fault_df[fault_df['Fault'] == 'normal'].groupby('Operator').size()
fault_counts = fault_df[fault_df['Fault'] == 'fault'].groupby('Operator').size()

if st.button("success rate"):
   
    success_rate = round((normal_counts / (normal_counts + fault_counts)) * 100)
    success_rate = success_rate.reset_index(name='success_rate')


    

    
    st.bar_chart(
        success_rate,
        x="Operator",
        y="success_rate",
        color="#87CEEB",
    )