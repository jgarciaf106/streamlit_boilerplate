import streamlit as st

class Page:
    def __init__(self, name, view_content, **kwargs):
        self.name = name
        self.view_content = view_content
        self.kwargs = kwargs

    def content(self):
        """Returns the content of the view by calling the view_content"""
        return self.view_content()

    def title(self):
        """Returns the title of the view"""
        st.header(f"{self.name}")

    def __call__(self):
        self.title()
        self.content()