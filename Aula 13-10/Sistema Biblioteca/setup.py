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

    # cursor.execute("SELECT VERSION();")
    # resultado = cursor.fetchall()
    # print(resultado)
    cursor.execute("DROP TABLE IF EXISTS livros;")
    cursor.execute("DROP TABLE IF EXISTS autores;")
    con.commit()

    cursor.execute('''
CREATE TABLE IF NOT EXISTS autores(
id_autor integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_autor varchar(255) NOT NULL
                   );
''')
    cursor.execute('''
CREATE TABLE IF NOT EXISTS livros(
id_livro integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
titulo_livro varchar(255) NOT NULL,
ano_livro integer NOT NULL,
autor_id integer NOT NULL,
CONSTRAINT fk_livro_autor FOREIGN KEY (autor_id) REFERENCES autores(id_autor)
)
''')
    con.commit()

    cursor.close()
    con.close()
    
except Exception as erro:
    print("ERRO DETECTADO -", erro)



