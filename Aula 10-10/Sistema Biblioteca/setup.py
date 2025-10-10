import psycopg2

DB_NAME = "Ecommerce"
DB_USER = "****"
DB_PASSWORD = "******"
DB_PORT = "******"
DB_HOST = "*******"

con = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)

cursor = con.cursor()

cursor.execute("SELECT * FROM clientes")
resultado = cursor.fetchall()
print(resultado)

cursor.close()
con.close()