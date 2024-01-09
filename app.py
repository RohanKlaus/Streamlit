import streamlit as st
import pandas as pd
import numpy as np
import time

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dict = {
  "name":["Sakshi"],
  "age":["20"],
  "city":["mumbai"]
}

data = pd.read_csv('Churn.csv')
print(data)

st.dataframe(data)
st.dataframe(data, width=500, height=500)
st.table(dict)
st.write(data)
st.write(dict)
st.json(a)

@st.cache
def ret_time():
  time.sleep(5)
  return time.time()

if st.checkbox("1"):
  st.write(ret_time())
  
if st.checkbox("2"):
  st.write(ret_time())

     
