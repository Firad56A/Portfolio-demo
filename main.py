import streamlit as st

st.set_page_config(layout="wide")

col1,  col2 = st.columns(2)
with col1:
    st.image("images/photo.png")

with col2:
    st.title("Firad Aslanov")
    content = """
    Hi I am Ardit! I am a python programmer. I have experience in Data and Web field. I am studying in RTU.
    """
    st.info(content)