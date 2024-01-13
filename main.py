import streamlit as st

st.set_page_config(layout="wide")

col1,  col2 = st.columns(2)
with col1:
    st.image("images/photo.png",width=500)

with col2:
    st.title("Firad Aslanov")
    content = """
    Hi I am Ardit! I am a python programmer. I have experience in Data and Web field. I am studying in RTU.
    """
    st.info(content)

contact = """
Below you can find some projects and apps. Feel free to contact me. I used Python and Tableu. I wanted to show my skills.
 """
st.write(contact)