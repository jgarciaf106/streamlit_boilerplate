import streamlit as st
import time
from app.core.page import Page
from app.core import snow_session
from streamlit_javascript import st_javascript


# TODO: allow a proper way to logout without error messages and reruns
# define the content of the view and render it inside the content function
def logout():
    if snow_session.close_session():
        # success message
        st.success("You have been logged out successfully!")
        st.rerun()


def content():
    # render content
    logout()


# create a view object and pass the content function
render = Page("", content)
