import streamlit as st
from streamlit_option_menu import option_menu
from .store import store


class ViewHandler:
    def __init__(self, views, logo):
        self.views = (
            [view for view in views if view["title"] != "Logout"]
            if not bool(store.get("log_status"))
            else [view for view in views]
        )
        self.view_names = (
            [view["title"] for view in views if view["title"] != "Logout"]
            if not bool(store.get("log_status"))
            else [view["title"] for view in views]
        )
        self.view_icons = [view["icon"] for view in views]
        self.logo = logo

    def view_selected(self, title, view_names, icons=None):
        with st.sidebar:
            # Create buttons for each view
            st.image(self.logo)

            default_index_val = st.session_state.get("view_idx", view_names[0])
            if default_index_val == "Logout":
                default_index_val = view_names[0]
            default_index = view_names.index(default_index_val)

            selected = option_menu(
                menu_icon="menu-app",
                menu_title=title,
                options=view_names,
                icons=icons,
                default_index=default_index,
                key="view_idx",
            )
            
            if selected == "Logout":
                selected = view_names[0]
                
            # TODO: show the information on the info box
            if bool(store.get("log_status")):
                st.divider()

                st.info(
                    """
                        ROLE: {0}  
                        
                        DATABASE: {1}
                        
                        SCHEMA: {2}
                        
                        WAREHOUSE: {3}
                        
                        """.format(
                        1, 2, 3, 4
                    )
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
            icons=self.view_icons,
        )

        st.experimental_set_query_params(view=selected_view)

        # run the selected app
        for view in self.views:
            if view["title"] == selected_view:
                view["function"]()


        #TODO FIx logout