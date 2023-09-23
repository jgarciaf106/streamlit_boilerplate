import streamlit as st
from app.utils.view_handler import ViewHandler
from app.views import home, settings, logout
from app.utils import snow_session
from app.utils.store import store

logo = "app/assets/logo.png"

st.set_page_config(
    page_title="Streamlit Boilerplate",
    page_icon=":blue_book:",
    layout="wide",
    initial_sidebar_state="expanded",
)
hide_st_footer = """
            <style>
            .main > div {padding-top: 0rem;}
            .css-e1vs0wn30 {padding-top: 0rem;}
            .css-10oheav {padding-top: 0rem; }
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_footer, unsafe_allow_html=True)
views = [
    {"title": "Home", "function": "home.render", "args": None, "icon": "house"},
    {"title": "Settings", "function": "settings.render", "args": None, "icon": "gear"},
    {"title": "Logout", "function": "logout.render", "args": None, "icon": "power"},
]
registered_views = [
    {
        "title": item["title"],
        "function": eval(item["function"]),
        "args": item["args"],
        "icon": item["icon"],
    }
    for item in views
]

view = ViewHandler(registered_views, logo)

def main():
    view.run()


if __name__ == "__main__":
    main()
