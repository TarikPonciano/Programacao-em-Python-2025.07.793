import psycopg2
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_HOST = os.getenv("DB_HOST")

try:
    con = psycopg2.connect(dbname=DB_NAME, host=DB_HOST, password=DB_PASSWORD, port=DB_PORT, user=DB_USER)
    cursor = con.cursor()

    #SQL AQUI

    cursor.close()
    con.close()
    
except Exception as erro:
    print("ERRO DETECTADO -", erro)



