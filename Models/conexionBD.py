import mariadb
from tkinter import messagebox

class ConexionBD():
    def __init__(self):
        self.__host = "localhost"
        self.__port = 3307 
        self.__user = "root"
        self.__password = "" 
        self.__database = "juego"
        self.__connection = None

    def getConnection(self):
        return self.__connection

    def crearConexion(self):
        try:
            self.__connection = mariadb.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                port=self.__port,
                database=self.__database
            )
            print(" Conexión exitosa a la base de datos.")
        except mariadb.Error as error:
            print(f" Error de conexión: {error}")
            messagebox.showwarning(
                "Advertencia",
                "Verifique su conexión a internet o al servidor local.\n"
                "Intente de nuevo más tarde o contacte al administrador del sistema."
            )

    def cerrarConexion(self):
        if self.__connection:
            self.__connection.close()
            self.__connection = None
            print(" Conexión cerrada correctamente.")
