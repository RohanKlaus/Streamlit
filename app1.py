import streamlit as st
import pandas as pd
import numpy as np
pip install matplotlib
import matplotlib.pyplot as plt


data = pd.DataFrame(
  np.random.randn(100,3),
  columns=['a','b','c']
)

st.write(data)

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)


plt.scatter(data['a'],data['b'])
st.pyplot
