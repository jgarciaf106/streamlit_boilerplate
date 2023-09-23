from app.core import snow_session


class SnowContext:
    def __init__(self) -> None:
        self.snow = snow_session.snowpark_session()

    def get_roles(self) -> list:
        try:
            roles = self.snow.sql(
                "SELECT VALUE::STRING FROM TABLE(FLATTEN(input => PARSE_JSON(CURRENT_AVAILABLE_ROLES())));"
            ).collect()
            roles = [role[0] for role in roles]
            return roles
        except Exception as e:
            print(f"Error getting roles: {e}")
            return []

    def get_databases(self, owner: str) -> list:
        try:
            dbs = self.snow.sql("SHOW DATABASES").collect()
            dbs = [db[1] for db in dbs if db[5] == owner]
            return dbs
        except Exception as e:
            print(f"Error getting databases: {e}")
            return []

    def get_schemas(self, db: str) -> list:
        try:
            schemas = self.snow.sql(f"SHOW SCHEMAS IN {db}").collect()
            schemas = [schema[1] for schema in schemas]
            return schemas
        except Exception as e:
            print(f"Error getting schemas: {e}")
            return []

    def get_warehouses(self) -> list:
        try:
            whs = self.snow.sql("SHOW WAREHOUSES").collect()
            whs = [wh[0] + " - " + wh[3] for wh in whs]
            return whs
        except Exception as e:
            print(f"Error getting warehouses: {e}")
            return []