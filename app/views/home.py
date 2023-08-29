import streamlit as st
from app.utils.page import Page


# define the content of the view inside the content function
def content():
    st.write("This is the content of the page.")
    
# create a view object and pass the content function
render = Page("Home Page", content)





