import streamlit as st
from typing import Callable


def error_handler(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            st.error(f"An error occurred: {e}")

    return wrapper


class Page:
    def __init__(self, view_title: str, view_content: Callable) -> None:
        self.__view_title = view_title
        self.__view_content = view_content

    def __title(self) -> None:
        st.header(f"{self.__view_title}")

    @error_handler
    def __content(self) -> None:
        self.__title()
        self.__view_content()

    def __call__(self) -> None:
        self.__content()