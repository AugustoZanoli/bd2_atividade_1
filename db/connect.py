import psycopg2

def connect():
        return psycopg2.connect(
                dbname="northwind",
                user="augusto_zanoli",
                password="Odisseia0!",
                host="localhost",
                port="5432"
        )