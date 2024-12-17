import streamlit as st
from database import db

if db not in st.session_state:
    st.session_state[db] = None

if db['username']:
    st.header(f"Welcome {db['username']}!")
else:
    st.header("Welcome Boss!")


# visibility_button = st.button("Show login details")