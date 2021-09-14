"""Database connection and general query function"""

from os import environ as env
from dotenv import load_dotenv
from psycopg2 import connect, DatabaseError
from psycopg2.extras import RealDictCursor as cursor_type

load_dotenv()

dbuser = env["POSTGRES_DB_USER"]
dbpassword = env["POSTGRES_DB_PASS"]
dbdb = env["POSTGRES_DB_DATA"]


def establish_connection(user, password, database):
    """Connects to a Postgres database

    Args:
        user (str): Database username
        password (str): Database password
        database (str): Database name

    Raises:
        RuntimeError: Error message in case connection can not be established

    Returns:
        connection: A connection to the database
    """

    try:
        connection = connect(f"postgres://{user}:{password}@127.0.0.1/{database}")
        # connection = connect(env["DATABASE_URL"], sslmode="require")
        connection.autocommit = True
        return connection

    except DatabaseError:
        raise RuntimeError("Could not connect to databse")


def query(statement, arguments=None):
    """Queries the database

    Args:
        statement (str): An SQL statement to be executed
        arguments (dict | tuple, optional): Variables to be injected. Defaults to None.

    Returns:
        RealDictRow: A list of tuples / dictionaries containing the query results
    """

    with establish_connection(dbuser, dbpassword, dbdb) as conn:
        with conn.cursor(cursor_factory=cursor_type) as cursor:
            cursor.execute(statement, arguments)

            return cursor.fetchall()
