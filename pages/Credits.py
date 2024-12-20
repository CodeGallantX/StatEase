import streamlit as st
from PIL import Image

st.set_page_config(
    page_title = "Credits - StatEase",
    page_icon="📜"
)

st.markdown(
    """
    <style>
        .social-icon {
            filter: invert(42%) sepia(79%) saturate(470%) hue-rotate(160deg) brightness(102%) contrast(97%);
            transition: transform 0.3s ease;
        }

        .social-icon:hover {
            transform: scale(1.2);
        }

        .profile-img {
            border-radius: 50%;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .profile-img:hover {
            transform: scale(1.1);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }

        a {
            text-decoration: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("## CodeGallantX - Software Developer")
st.write("----")
st.markdown("""<br/>""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    image = Image.open("Images/codegallantx.jpeg") 
    st.image(image, width=20, caption="CodeGallantX", use_column_width=False, output_format="PNG")

with col2:
    image = Image.open("Images/ydf_logo.png") 
    st.image(image, width=150, use_column_width=False, output_format="PNG")
    st.link_button(label="Yomi Denzel Foundation", url="https://yomidenzelfoundation.org.ng", type="tertiary")


st.write("### Connect with me")
st.write(
    """
    Follow me on my social media platforms for updates, insights, and more:
    """
)

col1, col2, col3, col4, col5 = st.columns(5)

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
with col5:
    st.markdown(
        """
        <a href="https://codegallantx.vercel.app">
            <span>Profile Link</span>
        </a>
        """, unsafe_allow_html=True
    )


st.markdown("""<br>""", unsafe_allow_html=True)

st.write("### Courtesy")
st.markdown(
    """
    We thank all contributors, collaborators, and the open-source community for their unwavering support in bringing this project to life.
    Special thanks to everyone who has provided feedback, ideas, and continuous motivation for improvements.
    """
)

st.write("---")
st.write("All Rights Reserved 2024 |", "Built with ❤️ by CodeGallantX")