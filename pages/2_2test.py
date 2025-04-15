import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# st.write('Привет')

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path)

st.dataframe(tips.head(10))

st.area_chart(tips, x='total_bill', y='tip', color='day')
