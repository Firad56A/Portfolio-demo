import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png",width=500)

with col2:
    st.title("Firad Aslanov")
    content = """
    Hi I am Firad! I am a python programmer. I have experience in Data and Web field. I am studying in RTU.
    """
    st.info(content)

contact = """
Below you can find some projects and apps. Feel free to contact me. I used Python and Tableu. I wanted to show my skills.
 """
st.write(contact)
col3,empty_col, col4 = st.columns([1.5, 0.5, 1.5])

dfs = pandas.read_csv("data.csv", sep=";")

with col3:
    for index , row in dfs[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index , row in dfs[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
