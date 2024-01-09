import streamlit as st

st.title("Registration Form")

first,last = st.columns(2)

first.text_input("First Name")
last.text_input("Last Name")

email,mob = st.columns([3,1])
email.text_input("Enter your Email")
mob.text_input("Mobile Number")

username,pw,pw2 = st.columns(3)
username.text_input("Enter your username")
pw.text_input("Enter your password", type="password")
pw2.text_input("Re-enter your password",type="password")

ch,bl,sub = st.columns(3)
ch.checkbox("I Agree")
sub.button("Submit")
