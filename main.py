import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.JPG")

with col2:
    st.title("Suneth Perera")
    content = """Hi, I am Suneth Perera, I am a Python Programmer!!!"""
    st.info(content)

content2 = """Below are some of the project that I have created so far!!!"""
st.write(content2)