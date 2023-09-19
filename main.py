import streamlit as st
from app.utils.view_handler import ViewHandler
from app.views import home, settings, logout
from app.utils import snow_session
from app.utils.store import store


### config the whole app
st.set_page_config(
    page_title="Streamlit Boilerplate",
    page_icon=":blue_book:",
    layout="wide",
    initial_sidebar_state="expanded",
)

hide_st_footer = """
            <style>
            .main > div {padding-top: 0rem;}
            .css-1629p8f {padding-top: 0rem;}
            .css-10oheav {padding-top: 0rem; }
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_footer, unsafe_allow_html=True)

### register view is done via pipenv run view command
view = ViewHandler()
view.add_view('Home', home.render)
view.add_view("Settings", settings.render)


# add logout button if credentials are set
if bool(store.get("log_status")):
    view.add_view('Logout', logout.render)

# *** entry point do not modify ***
def main():
    view.run()
    
if __name__ == "__main__":
    main()