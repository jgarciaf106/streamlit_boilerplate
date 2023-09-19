import streamlit as st
import time
from app.utils.page import Page
from app.utils import snow_session
from app.utils.store import store
from app.utils.snow_context import SnowContext


# define the content of the view and render it inside the content function
def toggle_closed():
    st.session_state["expander_state"] = True


def credentials(current_credentials):
    st.subheader("Snowflake Account")

    # form to handle initial loginf or fetch existing credentials
    with st.form("credentials_form", clear_on_submit=True):
        if "expander_state" not in st.session_state:
            st.session_state["expander_state"] = False

        with st.expander("Credentials", expanded=st.session_state["expander_state"]):
            # set credentials else show existing
            set_credentials = {
                "account": st.text_input(
                    "Account",
                    value=current_credentials["account"],
                    placeholder="e.g. abc123.us-east-1",
                ),
                "user": st.text_input(
                    "Username",
                    value=current_credentials["user"],
                    placeholder="e.g. snowflake_user",
                ),
                "password": st.text_input("Password", type="password"),
            }

        # save credentials on submit
        cred_submitted = st.form_submit_button("Sign in", on_click=toggle_closed)

        if cred_submitted:
            cred_status = snow_session.test_connection(set_credentials)
            if cred_status:
                # success message
                st.success("Connection successfull, credentials saved!")

                # close expander
                if st.session_state["expander_state"] == True:
                    st.session_state["expander_state"] = False
                    time.sleep(0.05)
                    st.experimental_rerun()
            else:
                st.error("All fields are required!")


def context(set_credentials):
    # allow user to be able to change the context
    
    if bool(store.get("log_status")):
        st.divider()
        st.subheader("Snowflake Account Context")

        left, center, right = st.columns(3)
        snow_context = SnowContext()

        with left:
            avail_roles = snow_context.get_roles()
            role = st.selectbox("Role", ["Switch Role"] + avail_roles)
            if role != "Switch Role":
                snow_session.set_context({"role": role})

        with center:
            avail_dbs = snow_context.get_databases()
            database = st.selectbox("Database", ["Switch Database"] + avail_dbs)
            if database != "Switch Database":
                snow_session.set_context({"database": database})
                avail_schemas = snow_context.get_schemas(database)
                schema = st.selectbox("Schema", ["Switch Schema"] + avail_schemas)
                if schema != "Switch Database":
                    snow_session.set_context({"schema": schema})

        with right:
            avail_whs = snow_context.get_warehouses()
            warehouse = st.selectbox("Warehouse", ["Switch Warehouse"] + avail_whs)
            if warehouse != "Switch Warehouse":
                snow_session.set_context({"warehouse": warehouse})


def content():
    print("Current Credentials: ", snow_session.get_credentials())
    # get existing credentials
    existing_credentials = snow_session.get_credentials()
    (
        cache_account,
        cache_user,
        cache_password,
        cache_role,
        cache_database,
        cache_schema,
        cache_warehouse,
    ) = existing_credentials.values()

    # render content
    credentials(existing_credentials)
    context(existing_credentials)


# create a view object and pass the content function
render = Page("Boilerplate Settings", content)
