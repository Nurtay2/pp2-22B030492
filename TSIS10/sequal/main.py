import psycopg2
from config import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port = 5432
    )
    connection.autocommit = True
    print("Connection established successfully!")
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(f"Server version: {cursor.fetchone()}")

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM phonebook""")
        print("[INFO] request was successfully filed")


except Exception as ex:
    print("[INFO] error occurred:", ex)
finally:
    if connection:
        connection.close()
        print("[INFO] connection closed")