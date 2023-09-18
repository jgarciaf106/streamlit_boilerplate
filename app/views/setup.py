import streamlit as st
import time
from app.utils.page import Page
from app.utils.session import SnowflakeSession


def toggle_closed():
    st.session_state["expander_state"] = True

    
    
def content():
    st.subheader("Snowflake Account")

    snow_session = SnowflakeSession("jwt_token_boilerplate")
    
    with st.form("credentials_form", clear_on_submit=True):
        if "expander_state" not in st.session_state:
            st.session_state["expander_state"] = False

        with st.expander("Credentials", expanded=st.session_state["expander_state"]):
            # get credentials
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
            
            print(existing_credentials)

            # Define the form fields
            snowflake_credentials = {
                "account": st.text_input("Account", value=cache_account, placeholder="e.g. abc123.us-east-1"),
                "user": st.text_input("User", value=cache_user, placeholder="e.g. snowflake_user"),
                "password": st.text_input("Password", type="password"),
                "role": st.text_input("Role", value=cache_role, placeholder="e.g. snowflake_role"),
                "database": st.text_input("Database", value=cache_database, placeholder="e.g. snowflake_db"),
                "schema": st.text_input("Schema", value=cache_schema, placeholder="e.g. snowflake_schema"),
                "warehouse": st.text_input("Warehouse", value=cache_warehouse, placeholder="e.g. snowflake_warehouse"),
            }

        submitted = st.form_submit_button(
            "Save Credentials",
            on_click=toggle_closed
        )
        # save credentials
        if submitted:
            cred_status = snow_session.test_connection(snowflake_credentials)
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


# create a view object and pass the content function
render = Page("Boilerplate Settings", content)