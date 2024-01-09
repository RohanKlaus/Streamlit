import streamlit as st
import pandas as pd

data = pd.read_csv("Churn.csv")

st.title("Telecommunication Churn")

nav = st.sidebar.radio("Navigation",["Visualisation","Predictor"])

if nav == ["Visualisation"]:
  st.write("Youre on visualisation page")

if nav == ["Predictor"]:
  st.write("Predict")
