import streamlit as st

st.title("Foster Home Matching")
st.write("Find the best foster home for your needs.")

st.page_link("pages/profiles.py", label="Profiles", icon="👤")
st.page_link("pages/matching.py", label="Matching", icon="🫂")