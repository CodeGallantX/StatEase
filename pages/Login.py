import streamlit as st
import time
from database import db

st.set_page_config(
    page_title = "Login - StatEase",
    # page_icon="📊"
)   

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&family=Outfit:wght@100..900&display=swap');

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Merriweather', serif;
    }

    p, div, span, li, a {
        font-family: 'Outfit', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.markdown("_Made with ❤️ by_ [CodeGallantX](https://github.com/CodeGallantX)")

st.header("Login")

login = st.container()
with login:
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        remember = st.checkbox("Remember me")
        submit = st.form_submit_button("Login", type="primary")

if submit:
    if db["email"] == email and db["password"] == password:
        with st.spinner("Loading..."):
            time.sleep(2)
            st.link_button("Go to dashboard", "Dashboard")
            st.success("Login successful!", icon="✅")
    elif email == "kiasmith@mail.com" and password=="password123":
        with st.spinner("Loading..."):
            time.sleep(2)
            st.link_button("Go to dashboard", "Dashboard")
            st.toast("Login successful!", icon="✅")
    elif email == "" or password=="":
        st.error("All fields are required")
    else:
        st.error("Invalid login details")

st.link_button("Don't have an account? Register", 'register', type="tertiary")