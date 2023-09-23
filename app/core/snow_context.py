from app.core import snow_session


class SnowContext:
    def __init__(self):
        self.snow = snow_session.snowpark_session()

    def get_roles(self):
        roles = self.snow.sql("SHOW ROLES").collect()
        roles = [role[1] for role in roles]
        return roles

    def get_databases(self):
        dbs = self.snow.sql("SHOW DATABASES").collect()
        dbs = [db[1] for db in dbs]
        return dbs

    def get_schemas(self, db):
        schemas = self.snow.sql(f"SHOW SCHEMAS IN {db}").collect()
        schemas = [schema[1] for schema in schemas]
        return schemas

    def get_warehouses(self):
        whs = self.snow.sql("SHOW WAREHOUSES").collect()
        whs = [wh[0] + " - " + wh[3] for wh in whs]
        return whs
