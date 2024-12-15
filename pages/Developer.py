import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Developer - CodeGallantX"
)

# Add custom CSS to change icon color and make the profile picture rounded
st.markdown(
    """
    <style>
        /* Change icon color */
        .social-icon {
            filter: invert(42%) sepia(79%) saturate(470%) hue-rotate(160deg) brightness(102%) contrast(97%);
        }
        
        /* Make profile picture more rounded */
        .profile-img {
            border-radius: 50%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Profile section
st.write("### CodeGallantX")

# Profile picture
image = Image.open("Images/codegallantx.jpeg")  # Replace with your image path
st.image(image, width=150, caption="CodeGallantX", use_column_width=False, output_format="PNG")

# Social Media Section
st.write("### Connect with me")
st.write(
    """
    Follow me on my social media platforms for updates, insights, and more:
    """
)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        """
        <a href="https://github.com/CodeGallantX">
            <img class="social-icon" src="https://img.icons8.com/ios-filled/50/000000/github.png" />
        </a>
        """, unsafe_allow_html=True
    )
with col2:
    st.markdown(
        """
        <a href="https://www.linkedin.com/in/john-samuel-cgx">
            <img class="social-icon" src="https://img.icons8.com/ios-filled/50/000000/linkedin.png" />
        </a>
        """, unsafe_allow_html=True
    )
with col3:
    st.markdown(
        """
        <a href="https://twitter.com/JohnSamue24013">
            <img class="social-icon" src="https://img.icons8.com/ios-filled/50/000000/twitter.png" />
        </a>
        """, unsafe_allow_html=True
    )
with col4:
    st.markdown(
        """
        <a href="https://www.instagram.com/johndayo227">
            <img class="social-icon" src="https://img.icons8.com/ios-filled/50/000000/instagram-new.png" />
        </a>
        """, unsafe_allow_html=True
    )

# Courtesy Section
st.write("### Courtesy")
st.markdown(
    """
    We thank all contributors, collaborators, and the open-source community for their unwavering support in bringing this project to life.
    Special thanks to everyone who has provided feedback, ideas, and continuous motivation for improvements.
    """
)

# Aim/Vision Section
st.write("### Aim / Vision")
st.markdown(
    """
    The primary aim of this project is to provide a tool that simplifies data analysis and helps users quickly process, visualize, and understand their data. 
    Our vision is to make data more accessible, educational, and easier to interpret for individuals, teams, and businesses.
    """
)

# Mission Section
st.write("### Mission")
st.markdown(
    """
    Our mission is to develop a user-friendly platform that empowers everyone, regardless of their background, to analyze and visualize data effectively. 
    We strive to continually improve the tool's functionality and interface to meet the needs of our users.
    """
)

# Footer Section
st.write("---")
st.write("Built with ❤️ by CodeGallantX")
