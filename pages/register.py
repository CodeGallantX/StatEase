import streamlit as st
import time
from database import db


st.set_page_config(
    page_title = "Register - StatEase",
    # page_icon=""
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

st.header("Register")


register = st.container()
with register:
    with st.form("signup_form"):
        db["username"] = st.text_input("Username")
        db["email"] = st.text_input("Email Address")
        db["password"] = st.text_input("Password", type="password")
        agree = st.checkbox("I agree to the terms and conditions.", value=False)
        submit = st.form_submit_button("Register", type="primary")


        if submit:
            if db["username"] == "" or db["password"] == "" or db["email"]:
                db["username"] == "" and db["password"] == "" and db["email"]
                st.error("All fields are required")
            elif db["username"] == db["username"] and db["password"] == db["password"] and db["email"] == db["email"]:
                db["username"] == db["username"] and db["password"] == db["password"] and db["email"] == db["email"]
                with st.spinner("Loading..."):
                    time.sleep(2)
                    st.link_button("Go to login page", "Login")
                    st.toast("Registration successful!", icon="✅")
            else:
                st.error("All fields are required")

st.link_button("Already have an account? Login", 'Login', type="tertiary")