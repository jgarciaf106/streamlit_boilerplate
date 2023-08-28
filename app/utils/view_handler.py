import streamlit as st

class ViewHandler:
    def __init__(self):
        self.views = []
        self.view_names = []

    def add_view(self, title, func, args=None):
        self.view_names.append(title)
        self.views.append({
            "title": title,
            "function": func,
            "args":args
        })

    def run(self):
        # get query_params
        query_params = st.experimental_get_query_params()
        choice = query_params["view"][0] if "view" in query_params else None

        # common key
        key = 'Navigation'

        # on_change callback
        def on_change():
            params = st.experimental_get_query_params()
            params['view'] = st.session_state[key]
            st.experimental_set_query_params(**params)

        # update session state
        st.session_state[key] = choice if choice in self.view_names else self.view_names[0]

        # Create buttons for each view
        st.sidebar.title("Navigation")
        for view in self.view_names:
            if view == st.session_state[key]:
                st.sidebar.button(view, key=view, use_container_width=True)
            else:
                if st.sidebar.button(view, use_container_width=True):
                    st.session_state[key] = view
                    on_change()

        # run the selected app
        for view in self.views:
            if view['title'] == st.session_state[key]:
                view['function']()
