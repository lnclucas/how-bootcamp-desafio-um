from sqlalchemy import create_engine, schema
CONN_STRING = 'postgresql://root:root@localhost:5455/db'


class Postgres:

    def __init__(self):
        self.engine = create_engine(CONN_STRING)
        self.connection = self.engine.raw_connection()

    def get_connection(self):
        return self.engine

    def create_pk(self, table_name, column_pk_name):
        cur = self.connection.cursor()
        cur.execute(f"ALTER TABLE {table_name} ADD PRIMARY KEY ({column_pk_name});")

    def close_connection(self):
        return self.connection.close()

    def creat_schema(self,schema_name):
        cur = self.connection.cursor()

        cur.execute(
            f"SELECT schema_name FROM information_schema.schemata WHERE schema_name = '{schema_name}'")
        result = cur.fetchone()

        if not result:
            cur.execute(f"CREATE SCHEMA {schema_name}")
            print(f"Schema {schema_name} criado com sucesso")

        self.connection.commit()

