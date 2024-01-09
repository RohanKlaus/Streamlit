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
st.date_input("Enter today's date")

#Time Input
st.time_input("Enter the time")

#Add a checkbox
if st.checkbox("You accept the T&C", value=False):
  st.write("Thankyou")

st.radio("Colors",['r','g','b'])
#st.radio("Colors",['r','g','b'],index=1)

st.selectbox("Colors",['r','g','b'])

st.multiselect("Colors",['r','g','b'])

st.slider("age", min_value=18, max_value=60, value=18, step=2)

st.number_input("numbers", min_value=18.0, max_value=60.0, value=30.0, step=2.0)

st.file_uploader("Upload a file")
