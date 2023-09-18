import streamlit as st
from streamlit_option_menu import option_menu


class ViewHandler:
    def __init__(self):
        self.views = []
        self.view_names = []

    def add_view(self, title, func, args=None):
        self.view_names.append(title)
        self.views.append({"title": title, "function": func, "args": args})

    def view_selected(self, title, view_names, icons=None):
        with st.sidebar:
            # Create buttons for each view
            st.image("app/assets/logo.png")
            
            default_index_val = st.session_state.get('view_idx', view_names[0])
            default_index = view_names.index(default_index_val)

            selected = option_menu(
                menu_icon="menu-app",
                menu_title=title,
                options=view_names,
                icons=icons,
                default_index=default_index,
                key='view_idx'
            )
            
        return selected

    def run(self):
        # get query_params
        query_params = st.experimental_get_query_params()
        choice = query_params["view"][0] if "view" in query_params else None

        # common key
        key = "Navigation"

        # update session state
        st.session_state[key] = (
            choice if choice in self.view_names else self.view_names[0]
        )

        selected_view = self.view_selected(
            title="Navigation",
            view_names=self.view_names,
            icons=["house", "gear", "file-plus"],
        )
        
        st.experimental_set_query_params(view=selected_view)

        # run the selected app
        for view in self.views:
            if view["title"] == selected_view:
                view["function"]()
