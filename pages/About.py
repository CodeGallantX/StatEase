import streamlit as st

st.set_page_config(
    page_title = "About - StatEase",
    page_icon="📊"
)


st.sidebar.markdown("_Made with ❤️ by_ [CodeGallantX](https://github.com/CodeGallantX)")


st.header("About")
st.write("---")

st.write("### Vision")
st.markdown(
    """
    The primary aim of this project is to provide a tool that simplifies data analysis and helps users quickly process, visualize, and understand their data. 
    Our vision is to make data more accessible, educational, and easier to interpret for individuals, teams, and businesses.
    """
)

st.markdown("""<br>""", unsafe_allow_html=True)

st.write("### Mission")
st.markdown(
    """
    Our mission is to develop a user-friendly platform that empowers everyone, regardless of their background, to analyze and visualize data effectively. 
    We strive to continually improve the tool's functionality and interface to meet the needs of our users.
    """
)
