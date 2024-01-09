import streamlit as st
import pandas as pd
import numpy as np



data = pd.DataFrame(
  np.random.randn(100,3),
  columns=['a','b','c']
)

st.write(data)

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

st.video('https://www.youtube.com/watch?v=jq0lKFb-P8k&list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5&index=4')

#plt.scatter(data['a'],data['b'])
#st.pyplot
