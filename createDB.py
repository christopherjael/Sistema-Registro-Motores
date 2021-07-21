import sqlite3

connection = sqlite3.connect('dbMotores.db')
cursor = connection.cursor()

def createDB():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Motores(
        Cedula VARCHAR(13) NOT NULL,
        Nombre VARCHAR(50) NOT NULL,
        Marca VARCHAR(50) NOT NULL,
        Modelo VARCHAR(50) NOT NULL,
        Placa VARCHAR(20) NOT NULL,
        Chasis VARCHAR(100) NULL,
        Telefono VARCHAR(13) NOT NULL,
        Direccion VARCHAR (100) NOT NULL,
        Latitud VARCHAR(100) NOT NULL,
        Longitud VARCHAR(100) NOT NULL,
        Actividad VARCHAR(50) NULL,
        Descripcion VARCHAR(255) NOT NULL,
        PRIMARY KEY(Cedula)
    );
    ''')

    connection.commit()
    connection.close()
    pass