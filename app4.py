import streamlit as st
import pandas as pd

data = pd.read_csv("Churn.csv")

st.title("Telecommunication Churn")

nav = st.sidebar.radio("Navigation",["Visualisation","Predictor"])

if nav == "Visualisation":
  st.image("https://github.com/RohanKlaus/project/blob/main/customer-churn.jpg",width=500)

if nav == "Predictor":
  st.write("Predict")
