import streamlit as st
import time

# Simulated database as a dictionary
db = {}

# Set page configuration
st.set_page_config(
    page_title="Register - StatEase",
    layout="centered"
)

# Apply custom styles
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
    unsafe_allow_html=True
)

# Sidebar content
st.sidebar.markdown("_Made with ❤️ by_ [CodeGallantX](https://github.com/CodeGallantX)")

# Page header
st.header("Register")

# Registration form
register = st.container()
with register:
    with st.form("signup_form"):
        username = st.text_input("Username")
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        agree = st.checkbox("I agree to the terms and conditions.", value=False)
        submit = st.form_submit_button("Register", type="primary")

    # Form submission handling
    if submit:
        if not username or not email or not password:
            st.error("All fields are required!")
        elif not agree:
            st.error("You must agree to the terms and conditions!")
        else:
            # Simulating database insertion
            db["username"] = username
            db["email"] = email
            db["password"] = password
            with st.spinner("Submitting your details..."):
                time.sleep(2)
            st.success("Registration successful!")
            st.markdown('[Go to Login Page](#)', unsafe_allow_html=True)

# Footer link for existing users
st.markdown(
    '<a href="#" style="text-decoration: none; color: #007bff;">Already have an account? Login</a>',
    unsafe_allow_html=True
)
