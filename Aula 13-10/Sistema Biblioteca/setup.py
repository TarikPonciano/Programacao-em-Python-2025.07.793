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
    cursor.execute("DROP TABLE IF EXISTS alugueis;")
    cursor.execute("DROP TABLE IF EXISTS livros;")
    cursor.execute("DROP TABLE IF EXISTS autores;")
    cursor.execute("DROP TABLE IF EXISTS membros;")
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
);
''')
    cursor.execute('''
CREATE TABLE IF NOT EXISTS membros(
id_membro integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_membro varchar(255) NOT NULL,
email_membro varchar(255) CHECK(email_membro LIKE '%@%')
);
''')
    
    cursor.execute('''
CREATE TABLE IF NOT EXISTS alugueis (
id_aluguel integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
membro_id integer NOT NULL,
livro_id integer NOT NULL,
data_aluguel date DEFAULT current_date,
data_devolucao date,
CONSTRAINT fk_aluguel_membro FOREIGN KEY (membro_id) REFERENCES membros(id_membro),
CONSTRAINT fk_aluguel_livro FOREIGN KEY (livro_id) REFERENCES livros(id_livro)      
);
''')
    con.commit()

    cursor.execute('''
INSERT INTO autores
VALUES (default, 'J.R Tolkien'), (default, 'George Martin'), (default, 'Machado de Assis');
''')
    con.commit()

    cursor.close()
    con.close()
    
except Exception as erro:
    print("ERRO DETECTADO -", erro)



