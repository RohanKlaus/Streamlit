import streamlit as st
import pandas as pd

data = pd.read_csv("Churn.csv")

st.title("Telecommunication Churn")

nav = st.sidebar.radio("Navigation",["Visualisation","Predictor"])

if nav == "Visualisation":
  st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fimpact-churn-telecom-industry-how-bi-can-potentially-solve-chowdary&psig=AOvVaw0Ft646Mhn3u9P2oxQ8WnGr&ust=1704921311683000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCLjEzfyc0YMDFQAAAAAdAAAAABAD",width=500)

if nav == "Predictor":
  st.write("Predict")
