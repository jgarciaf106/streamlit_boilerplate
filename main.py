import streamlit as st
from app.utils.view_handler import ViewHandler
from app.views import landing

# ---------------------------------
# --- modify only section start ---
# ---------------------------------

### config the whole app
st.set_page_config(
    page_title="Streamlit Boilerplate",
    page_icon=":blue_book:",
    layout="wide",
    initial_sidebar_state="expanded",
)

### Add views to be run on the app
view = ViewHandler()
view.add_view('Home', landing.render)

# ---------------------------------
# --- modify only section end ---
# ---------------------------------

# *** entry point do not modify ***
def main():
    view.run()
    
if __name__ == "__main__":
    main()