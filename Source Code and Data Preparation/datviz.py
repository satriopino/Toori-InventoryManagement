import streamlit as st
import numpy as np
from variables import next_2weeks_dates
import pandas as pd

st.set_page_config(page_title="Data Visualization", page_icon="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/microsoft/74/delivery-truck_1f69a.png", layout="wide", menu_items=None)

st.markdown("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="../static/style_datviz.css">
  <title>Document</title>
    <style>
        .block-container {
            background-color: #e4e9f7 !important;
        }
    </style>
</head>
<body>
<h2 style="margin-top: -75px;">Data Visualization</h2>
</body>
</html>
""", unsafe_allow_html = True)

with open("../next_sequence.npy", 'rb') as f:
    sequence = np.load(f)

data = pd.read_csv("../data/sparse_store_nbr_1.csv")
data_with_date = data.set_index("date").copy()

col1, col2 = st.columns(2)
with col1:
    for i in data_with_date.columns[:len(data_with_date.columns) // 2]:
        st.write(i)
        st.line_chart(data_with_date.iloc[-14:, np.argmax(data_with_date.columns == i)])
        st.write("")
        st.write("")

with col2:
    for i in data_with_date.columns[len(data_with_date.columns) // 2: ]:
        st.write(i)
        st.line_chart(data_with_date.iloc[-14:, np.argmax(data_with_date.columns == i)])
        st.write("")
        st.write("")

