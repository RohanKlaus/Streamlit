import streamlit as st
import pandas as pd
import numpy as np


data = pd.DataFrame(
  np.random.randn(100,3),
  columns=['a','b','c']
)

st.write(data)
