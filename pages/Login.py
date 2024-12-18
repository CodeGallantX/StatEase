import streamlit as st
import time
from database import db  # Ensure database.py exists in the same directory

st.set_page_config(
    page_title="Login - StatEase",
    layout="centered",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900&family=Outfit:wght@100..900&display=swap');

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Merriweather', serif;
    }

    p, div, span, li, a {
        font-family: 'Outfit', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar branding
st.sidebar.markdown("_Made with ❤️ by_ [CodeGallantX](https://github.com/CodeGallantX)")

# Page Header
st.header("Login")

# Login form container
login = st.container()
with login:
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        remember = st.checkbox("Remember me")
        submit = st.form_submit_button("Login")

if submit:
    if email == "" or password == "":
        st.error("All fields are required.")
    elif email == db.get("email") and password == db.get("password"):
        # Simulated login using database values
        with st.spinner("Loading..."):
            time.sleep(2)
        st.success("Login successful!")
        st.button("Go to Dashboard")
    elif email == "kiasmith@mail.com" and password == "password123":
        # Hardcoded fallback credentials
        with st.spinner("Loading..."):
            time.sleep(2)
        st.success("Login successful!")
        st.button("Go to Dashboard")
    else:
        st.error("Invalid login details.")

# Link for new users
st.markdown("[Don't have an account? Register](#)")
