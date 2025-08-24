# Requisitos: Desarrollar estos dos puntos a lo largo de las 2 horas de clase
# 1. Recordando la estructura de las clases como lo es para la clase (DatabaseConnection)

# Herencia: Es un principio de la programación orientada a objetos (POO) que permite crear nuevas clases basadas en clases existentes, 
#           heredando sus atributos y métodos.

# Polimorfismo: Es la capacidad de los objetos de diferentes clases relacionadas por herencia de responder de manera distinta al mismo método, 
#               permitiendo usar una interfaz común.

import sqlite3
import psycopg2

# Clase
class DatabaseConnection:
    def __init__(self, db_name):
        #Atrubutos
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        #Manejo de errores
        raise NotImplementedError("Subclasses must implement connect()")

    def execute_query(self, query, params=()):
        if not self.conn:
            raise Exception("Database not connected.")
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor

    def fetch_all(self, query, params=()):
        result = self.execute_query(query, params)
        return result.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

# Herencia de la clase DatabaseConnection para usarla como base para crear SQLiteConnection
class SQLiteConnection(DatabaseConnection):
    def __init__(self, db_name=":memory:"):
        super().__init__(db_name)

    def connect(self):  # Polimorfismo
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        print(f"Connected to SQLite database: {self.db_name}")

# Herencia de la clase DatabaseConnection para usarla como base para crear PostgresConnection
class PostgresConnection(DatabaseConnection):
    def __init__(self, db_name, user, password, host="localhost", port=5432):
        #Se usa super para hacer el llamado del constructor DatabaseConnection
        super().__init__(db_name)
        #Se agregan valores necesarios para el uso correcto de una base de datos como postgresql
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):  # Polimorfismo
        self.conn = psycopg2.connect(
            dbname = self.db_name,
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port
        )
        self.cursor = self.conn.cursor()
        print(f"Connected to PostgreSQL database: {self.db_name}")
        
#Cada una de los métodos que tiene DatabaseConnection, los puede usar SQLiteConnection y PostgresConnection

# Ahora llevemoslo al mundo real, necesitamos un manejador de archivos que pidió un cliente para su uso personal, por ende se debe crear un clase que cumpla las necesidades
# del cliente:

# Para esto se necesita:
# 1. Crear una clase llamada FolderManager (No debe tener atributos)
# 2. Que tenga métodos para: Crear carpetas, ver qué carpetas hay y por último borrar las carpetas
# 3. Los nombres de los métodos y de los atributos están mal escritos lo ideal es dejarlos con un nombre correcto para que cualquier dev pueda leerlo bien.

# Para este caso se recomienda investigar la librería os para el manejo de archivos


import os

class FolderManager:
    #Para el constructor viene solo el path (path: ruta donde se desea realizar los cambios)
    def __init__(self, p):
        #Crear el constructor con el atributo dado
        ...
    #Metodo para crear una carpeta
    def cfld(self, f):
        #Se debe ir mostrando en pantalla por medio de print las funciones realizadas
        #print(Se creó la carpeta de manera correcta)
        ...
    #Metodo listar las carpetas
    def ls(self):
        ...

    #Metodo para borrar las carpetas
    def d(self, f):
        #print(Se eliminó la carpeta de manera correcta)
        ...
