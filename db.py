import psycopg2

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname="YOUR DB",
            user="postgres",
            password="YOUR PASSWORD",
            host="localhost",
            port="5432"
        )
        print("Connected to database successfully")
        return connection
    except psycopg2.Error as e:
        print(f"Unable to connect to the database: {e}")
        return None