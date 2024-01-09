import streamlit as st
import pandas as pd

data = pd.read_csv("Churn.csv")

st.title("Telecommunication Churn")

nav = st.sidebar.radio("Navigation",["Visualisation","Predictor"])

if nav == "Visualisation":
  st.image("https://github.com/RohanKlaus/project/blob/main/customer-churn.jpg",width=800)

st.text_input("Which kind of graph do you want?",["Interactive","Non-interactive"])

if nav == "Predictor":
  st.write("Predict")
