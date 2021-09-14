from dotenv import load_dotenv
from os import environ as env
load_dotenv()

dbuser = env["POSTGRES_DB_USER"]
dbpassword = env["POSTGRES_DB_PASS"]
dbdb = env["POSTGRES_DB_DATA"]

def establish_connection(user, password, db):
    from psycopg2 import connect, DatabaseError

    try:
        connection = connect(f"postgres://{user}:{password}@127.0.0.1/{db}")
        connection = connect(env["DATABASE_URL"], sslmode="require")
        connection.autocommit = True
        return connection

    except DatabaseError:
        raise RuntimeError("Could not connect to databse")


def query(statement, vars=None):
    from psycopg2.extras import RealDictCursor as cursor_type

    with establish_connection(dbuser, dbpassword, dbdb) as conn:
        with conn.cursor(cursor_factory=cursor_type) as cursor:
            cursor.execute(statement, vars)

            return cursor.fetchall()
