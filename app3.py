import streamlit as st
import pandas as pd

st.title("Registration Form")

first,last = st.beta_columns(2)

first.text_input("First Name")
last.text_input("Last Name")
