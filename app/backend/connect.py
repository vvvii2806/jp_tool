import os
import psycopg2
from  dotenv import load_dotenv, find_dotenv



def create_cursor():
    load_dotenv(find_dotenv())
    connection = psycopg2.connect(
            dbname =os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASS"),
            port = os.getenv("DB_PORT"),
            host = os.getenv("DB_HOST")
        )
    cursor = connection.cursor()

    return cursor, connection


def close_env(cursor, connection):
    cursor.close()
    connection.close()
    return


def print_rows(cursor, rows):
    if not cursor or not cursor.description:
        print("Empty cursor")
        return
    
    cols = [d[0] for d in cursor.description]
    
    widths = [max(len(str(x)) for x in col) for col in zip(cols, *rows)]
    
    header = " | ".join(f"{c:<{w}}" for c, w in zip(cols, widths))
    print(header)
    print("-" * len(header))
    
    for row in rows:
        print(" | ".join(f"{str(v):<{w}}" for v, w in zip(row, widths)))    