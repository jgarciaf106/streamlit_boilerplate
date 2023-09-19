import streamlit as st
from app.utils.page import Page


# define the content of the view and render it inside the content function
def example():
    st.write("This is the content of the page.")


def content():
    # render content
    example()


# create a view object and pass the content function
render = Page("Home Page", content)
