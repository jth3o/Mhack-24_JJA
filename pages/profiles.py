import streamlit as st

st.page_link("home.py", label="Home", icon="🏠")

st.title("Your Profile")
name = st.text_input("Foster Home Name")
location = st.text_input("Location")
if st.button("Submit"):
    st.write(f"Profile created for {name} located in {location}.")