import json
import streamlit as st
import jwt
from snowflake.snowpark import Session
from datetime import datetime, timedelta
from .store import store


class SnowflakeSession:
    def __init__(self, app_key: str) -> None:
        self.key = app_key
        self.secret = st.secrets.jwt_key
        self.snowflake_credentials = None
        self.snowflake_session = None

    def __set_to_local_storage(self, value: str, ttl: int):
        try:
            expiry_time = datetime.now() + timedelta(seconds=ttl)

            # Construct the cookie_data as a Python dictionary
            cookie_data = {"value": value, "expiry": int(expiry_time.timestamp() * 1000)}

            # Convert the dictionary to a JSON string
            cookie_data_json = json.dumps(cookie_data)

            # store on local store
            store.set(self.key, cookie_data_json)
        except Exception as e:
            st.error(f"Error setting value to local storage: {e}")

    def __get_from_local_storage(self) -> dict:
        try:
            json_data = store.get(self.key)

            if not json_data:
                return {}

            current_datetime = datetime.now()
            now = int(current_datetime.timestamp())

            # parse the JSON string to a Python dictionary
            json_data = json.loads(json_data)

            if now > json_data["expiry"]:
                store.delete(self.key)
                return {}

            return json_data["value"]
        except Exception as e:
            st.error(f"Error getting value from local storage: {e}")
            return {}

    def __encode_jwt(self, value: dict, ttl: int):
        try:
            token = jwt.encode(value, self.secret, algorithm="HS256")
            self.__set_to_local_storage(token, ttl)
        except Exception as e:
            st.error(f"Error encoding JWT: {e}")

    def __decode_jwt(self) -> dict:
        try:
            jwt_token = self.__get_from_local_storage()

            if not jwt_token:
                return {
                    "account": "",
                    "user": "",
                    "password": "",
                    "role": "",
                    "database": "",
                    "schema": "",
                    "warehouse": "",
                }

            decoded_payload = jwt.decode(jwt_token, self.secret, algorithms=["HS256"])
            read_credentials = {
                "account": decoded_payload.get("account"),
                "user": decoded_payload.get("user"),
                "password": decoded_payload.get("password"),
                "role": decoded_payload.get("role"),
                "database": decoded_payload.get("database"),
                "schema": decoded_payload.get("schema"),
                "warehouse": decoded_payload.get("warehouse"),
            }

            return read_credentials
        except jwt.ExpiredSignatureError:
            st.write("Token has expired.")
            return {}
        except jwt.InvalidTokenError:
            st.write("Invalid token.")
            return {}
        except Exception as e:
            st.error(f"Error decoding JWT: {e}")
            return {}

    def test_connection(self, snowflake_credentials: dict) -> bool:
        status = False
        # test connection
        try:
            # Create a session object
            with st.spinner("Testing Connection..."):
                snow = Session.builder.configs(snowflake_credentials).create()

                # test connection
                res = snow.sql("Select current_account();").collect()

                if res[0][0].lower() == snowflake_credentials["account"].split(".")[0]:
                    self.__encode_jwt(snowflake_credentials, 3600)
                    store.set("log_status", "True")
                    status = True

        except Exception as e:
            st.error("Connection failed. Please check your credentials.")
            st.error(f"Error testing connection: {e}")
            raise e

        return status

    def get_credentials(self) -> dict:
        try:
            get_credentials = self.__decode_jwt()
            return get_credentials
        except Exception as e:
            st.error(f"Error getting credentials: {e}")
            return {}

    def set_context(self, credential_update: dict):
        try:
            snowflake_credentials = self.get_credentials()

            # get the key and value from the credential_update
            for key, value in credential_update.items():
                # update the value of the key
                snowflake_credentials[key] = value

            self.__encode_jwt(snowflake_credentials, 3600)
        except Exception as e:
            st.error(f"Error setting context: {e}")

    def snowpark_session(self) -> Session:
        try:
            get_credentials = self.__decode_jwt()
            snow = Session.builder.configs(get_credentials).create()
            return snow
        except Exception as e:
            st.error(f"Error creating Snowpark session: {e}")
            return None

    def close_session(self) -> bool:
        try:
            store.delete(self.key)
            store.delete("log_status")
            return True

        except Exception as e:
            st.error(f"Error closing session: {e}")
            return False
