import psycopg2

class ConexaoDB():
    def __init__(self, dbname, host, port, user, password):
        self.dbname = dbname
        self.host = host
        self.port = port
        self.user = user
        self.password = password

        self.conn = None
        self.cursor = None

    def consultar(self, sql, vars):
        self.conectar()

        try:
            # Consulta SQL
            self.cursor.execute(sql, vars)
            resultado = self.cursor.fetchall()
        except Exception as e:
            print("Erro ConexãoDB - Erro de Consulta:", e)
            resultado = None

        self.desconectar()

        return resultado

    def manipular(self, sql, vars):
        self.conectar()
        resultado = None
        try:
            self.cursor.execute(sql, vars)
            self.conn.commit()
            resultado = "DEU CERTO!"

        except Exception as e:
            print("Erro ConexãoDB - Erro de Manipulação:", e)
            self.conn.rollback()
            resultado = "DEU ERRADO!"

        self.desconectar()

        return resultado

    def conectar(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname, host=self.host, port=self.port, user=self.user, password=self.password)

            self.cursor = self.conn.cursor()
        except Exception as e:
            print("Erro ConexãoDB - Erro de Conexão:", e)

            self.desconectar()

    def desconectar(self):
        try:
            if self.cursor:
                self.cursor.close()
        except Exception as e:
            print("Erro ConexãoDB - Erro de Desconexão:", e)
            self.cursor = None

        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            print("Erro ConexãoDB - Erro de Desconexão:", e)
            self.conn = None