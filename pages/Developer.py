import streamlit as st
from PIL import Image

# Update session state with the selected page


# Developer/Credits Page
st.session_state.current_page == "Developer/Credits"
st.subheader("Developer / Credits")

# Profile section
st.write("### Developer: CodeGallantX")

# Profile picture
image = Image.open("Images/codegallantx.jpeg")  # Replace with your image path
st.image(image, width=150, caption="CodeGallantX")

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
        [![GitHub](Images/github.png)](https://github.com/CodeGallantX)
        """
    )
with col2:
    st.markdown(
        """
        [![LinkedIn](https://img.icons8.com/ios-filled/50/000000/linkedin.png)](https://www.linkedin.com/in/samuel-ayobami-john)
        """
    )
with col3:
    st.markdown(
        """
        [![Twitter](https://img.icons8.com/ios-filled/50/000000/twitter.png)](https://twitter.com/your_username)
        """
    )
with col4:
    st.markdown(
        """
        [![Instagram](https://img.icons8.com/ios-filled/50/000000/instagram-new.png)](https://www.instagram.com/your_username)
        """
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
st.write("Built with ❤️ by Samuel Ayobami John")
