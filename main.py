import numpy as np
import pandas as pd

import streamlit as st


st.title('success_rate by operator')
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
#하나의 파일을 업로드하는코드
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
 
    # To read file as string:
    string_data = stringio.read()
    #업로드한파일을 데이터프레임으로 읽어오고
    df = pd.read_csv(uploaded_file)
    #페이지에 출력
    st.dataframe(df)
    
# df = pd.read_csv('Piece_Dimension.csv')

#버튼을 누르면 df에 부피를 입력하고 부피가 일정범위를 벗어나면 fault 정상이면 nomal을 추가
if st.button("success rate"):
    df['Volume'] =(df['Length'] *  df['Width'] *  df['Height']).astype(int)
    df['Fault'] = [ 'normal' if 91134 < volume < 109242 else 'fault' for volume in df['Volume']]
    st.dataframe(df)
    #df에서 ['Operator', 'Fault'] 열만 추출 
    fault_df = df[['Operator', 'Fault']]
    #오퍼레이터별 정상과 불량의수를 세기
    normal_counts = fault_df[fault_df['Fault'] == 'normal'].groupby('Operator').size()
    fault_counts = fault_df[fault_df['Fault'] == 'fault'].groupby('Operator').size()
    #성공률을 계산해서 success_rate 에입력
    success_rate = round((normal_counts / (normal_counts + fault_counts)) * 100)
    # 성공률이 들어가는 열 이름을 success_rate로 지정
    success_rate = success_rate.reset_index(name='success_rate')
    #오퍼레이터별 성공률 그래프 출력
    st.bar_chart(
        success_rate,
        x="Operator",
        y="success_rate",
        color="#87CEEB",
    )
