import streamlit as st

#Title
st.title('Widgets')

#Button
if st.button('Subscribe'):
  st.write('Like this Video')

#Text Input
name = st.text_input("Name")
st.write(name)

#Text Area
address = st.text_area("Enter your address")
st.write(address)

#Date Input
date = st.date_input("Enter today's date")
st.wrtie(date)
