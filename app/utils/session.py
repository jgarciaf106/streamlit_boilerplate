import os
import time
import streamlit as st
import jwt
from snowflake.snowpark import Session


def set_credentials(snowflake_credentials):
    valid_summit = False
    # check if all fields are filled
    with st.spinner('Testing Connection...'):
        test_status = test_connection(snowflake_credentials)

    if test_status:
        # save credentials using jwt and session state
        token = jwt.encode(snowflake_credentials, st.secrets.jwt_key, algorithm="HS256")

        if "jwt_token" not in st.session_state:
            st.session_state.jwt_token = token

        valid_summit = True
    return valid_summit


def get_credentials():
    credentials = {
        "account": "",
        "user": "",
        "password": "",
        "role": "",
        "database": "",
        "schema": "",
    }
    if "jwt_token" in st.session_state:
        jwt_token = st.session_state.jwt_token

        try:
            # Verify and decode the JWT token
            decoded_payload = jwt.decode(
                jwt_token, st.secrets.jwt_key, algorithms=["HS256"]
            )

            # Access the data within the payload
            credentials = {
                "account": decoded_payload.get("account"),
                "user": decoded_payload.get("user"),
                "password": decoded_payload.get("password"),
                "role": decoded_payload.get("role"),
                "database": decoded_payload.get("database"),
                "schema": decoded_payload.get("schema"),
            }

        except jwt.ExpiredSignatureError:
            # Token has expired
            print("Token has expired.")
        except jwt.InvalidTokenError:
            # Token is invalid or tampered with
            print("Invalid or tampered token.")

    return credentials


def test_connection(snowflake_credentials):
    status = False
    # test connection
    try:
        # Create a session object
        snow = Session.builder.configs(snowflake_credentials).create()
        # test connection
        res = snow.sql("Select current_account();").collect()

        if res[0][0].lower() == snowflake_credentials["account"].split(".")[0]:
            status = True
    except Exception as e:
        st.error("Connection failed. Please check your credentials.")

    return status


