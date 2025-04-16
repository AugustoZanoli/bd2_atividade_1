import psycopg2

def connect():
        conn= psycopg2.connect(
                dbname="northwind",
                user="augusto_zanoli",
                password="Odisseia0!",
                host="localhost",
                port="5432"
        )

        #Tive que colocar o autocommit aqui para simular a injection no banco
        conn.autocommit = True
        return conn