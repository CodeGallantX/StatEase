import streamlit as st
import config
import font
from PIL import Image



# Add custom CSS for animations, icon color change, and rounded profile picture
st.markdown(
    """
    <style>
        /* Change icon color */
        .social-icon {
            filter: invert(42%) sepia(79%) saturate(470%) hue-rotate(160deg) brightness(102%) contrast(97%);
            transition: transform 0.3s ease;
        }

        /* Add hover animation for social icons */
        .social-icon:hover {
            transform: scale(1.2);
        }

        /* Make profile picture more rounded and add animation */
        .profile-img {
            border-radius: 50%;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        /* Hover effect for profile picture */
        .profile-img:hover {
            transform: scale(1.1);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and profile section
st.write("### [CodeGallantX](https://codegallantx.vercel.app)")

# Profile picture with rounded corners and hover animation
image = Image.open("Images/codegallantx.jpeg")  # Replace with your image path
st.image(image, width=150, caption="CodeGallantX", use_column_width=False, output_format="PNG")

# Social Media Section
st.write("### Connect with me")
st.write(
    """
    Follow me on my social media platforms for updates, insights, and more:
    """
)

# Using columns for social media icons
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        """
        <a href="https://github.com/CodeGallantX">
            <img class="social-icon" src="../Images/github.png" />
        </a>
        """, unsafe_allow_html=True
    )
with col2:
    st.markdown(
        """
        <a href="https://www.linkedin.com/in/john-samuel-cgx">
            <img class="social-icon" src="../Images/linkedin.png" />
        </a>
        """, unsafe_allow_html=True
    )
with col3:
    st.markdown(
        """
        <a href="https://twitter.com/JohnSamue24013">
            <img class="social-icon" src="https://cdn-icons-png.freepik.com/256/5969/5969020.png" />
        </a>
        """, unsafe_allow_html=True
    )
with col4:
    st.markdown(
        """
        <a href="https://www.instagram.com/johndayo227">
            <img class="social-icon" src="../Images/instagram.png" />
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
