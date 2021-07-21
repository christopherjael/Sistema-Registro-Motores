import sqlite3
from sqlite3.dbapi2 import enable_shared_cache
import folium
from geopy.geocoders import Nominatim
import webbrowser
import os
from prettytable import from_db_cursor, PrettyTable

#CREATE CONNECTION WITH DATABASE
connection = sqlite3.connect('dbMotores.db')
cursor = connection.cursor()

#CREATE MAPA WITH FOLIUM
mapa = folium.Map(location=[18.5109567,-69.8709899], zoom_start=12)
tooltip = 'Ver Información'

#GEOPY
geolocator = Nominatim(user_agent="Registro_Motores")

#prettytable
tableFormt = PrettyTable()

def limpiar():
    os.system('cls')
    pass



def verMotores():
    connection = sqlite3.connect('dbMotores.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Motores')
    tableFormt = from_db_cursor(cursor)
    print(tableFormt)
    pass



def verMotoresMapa():
    lat = ''
    lon = ''
    for rows in cursor.execute('SELECT * FROM Motores'):
        lat = rows[8]
        lon = rows[9]
        folium.Marker(
            [float(lat), float(lon)],
            popup=f'<i>{rows[0]}, {rows[1]}, {rows[2]}, {rows[3]}, {rows[4]}</i>', 
            tooltip=tooltip,
            icon=folium.Icon(icon="motorcycle", prefix="fa", color="blue")
        ).add_to(mapa)
        pass

    mapa.save('index.html')
    webbrowser.open('index.html')
    pass



def registrarMotor():
    print('---- Registrar Motor ----')
    print('Lista de Motores Registrados')
    verMotores()
    cedula = input('Introce la CEDULA del chofer, o deje vacio para no registrar nada\n> ')
    nombre = input('Introce el NOMBRE del chofer\n> ')
    marca = input('Introce la MARCA del Motor\n> ')
    modelo = input('Introce el MODELO del Motor\n> ')
    placa = input('Introce la PLACA del Motor\n> ')
    chasis = input('Introce el nombre del CHASIS del motor\n> ')
    telefono = input('Introce el NÚMERO de telefono del chofer\n> ')
    direccion = input('Introce la DIRECCION del chofer\n> ')
    while True:
        latitud = input('Introce la LATITUD de la ubicación del chofer\n> ')
        longitud = input('Introce la LONGITUD de la ubicación del chofer\n> ')
        location = geolocator.reverse(f"{latitud}, {longitud}")
        ubicacion = location.address
        if 'República Dominicana' in ubicacion:
            actividad = input('Introce la ACTIVIDAD que realiza el chofer con el motor\n> ')
            descripcion = input('Introce la DESCRIPCION del Motor\n> ')
            
            cursor.execute(f"""
            INSERT INTO Motores VALUES
            ('{cedula}',
            '{nombre}',
            '{marca}',
            '{modelo}',
            '{placa}',
            '{chasis}',
            '{telefono}',
            '{direccion}',
            '{latitud}',
            '{longitud}',
            '{actividad}',
            '{descripcion}');
            """)
            connection.commit()
            print('REGISTRO COMPLETO')
            input('Presiona ENTER para volver al MENU principal')
            break
        else:
            limpiar()
            print('LAS CORDENADAS QUE ACABA DE INTRODUCIR NO SON DE REPUBLICA DOMINICANA, POR FAVOR INTENTE DE NUEVO')
            pass
        pass
    pass

def cambiarDato(nombreCampo, valor):
    nv = input(f'Introduce el {nombreCampo}, o pude dejar vacio para no cambiar el valor actual\n> ')
    if nv == '':
        return valor
    else:
        return nv

    


def modificarMotor():
    print('---- Modificar Motor ----')
    print('Lista de Motores Registrados')
    verMotores()
    cedula = input('Introduce la cedula del Motor que quiere Modificar\n> ')
    usuarioExiste = False
    for rows in cursor.execute(f"SELECT Cedula, Nombre FROM Motores WHERE Cedula = '{cedula}'"):
        if rows:
            usuarioExiste = True
            pass
        pass

    if usuarioExiste:
        limpiar()
        print('El Usuario existe y esta es su información')
        cursor.execute(f"SELECT * FROM Motores WHERE Cedula = '{cedula}'")
        tableFormt = from_db_cursor(cursor)
        print(tableFormt)

        datosActual = ()
        for row in cursor.execute(f"SELECT * FROM Motores WHERE Cedula = '{cedula}'"):
            datosActual = row
            pass

        cedula = cambiarDato('Cedula',datosActual[0])
        nombre = cambiarDato('Nombre', datosActual[1])
        marca = cambiarDato('Marca', datosActual[2])
        modelo = cambiarDato('Modelo', datosActual[3])
        placa = cambiarDato('Placa', datosActual[4])
        chasis = cambiarDato('Chasis', datosActual[5])
        telefono = cambiarDato('Telefono', datosActual[6])
        direccion = cambiarDato('Direccion', datosActual[7])
        latitud = cambiarDato('Latitud', datosActual[8])
        longitud = cambiarDato('Longitud', datosActual[9])
        actividad = cambiarDato('Actividad', datosActual[10])
        descripcion = cambiarDato('Descripcion', datosActual[11])

        if nombre == '':
            print('MODIFICACION CANCELADA')
            input('Presiona ENTER para volver al MENU principal')

        else:
            cursor.execute(f"""
            UPDATE Motores
            SET
            Cedula = '{cedula}',
            Nombre = '{nombre}',
            Marca = '{marca}',
            Modelo = '{modelo}',
            Placa = '{placa}',
            Chasis = '{chasis}',
            Telefono = '{telefono}',
            Direccion = '{direccion}',
            Latitud = '{latitud}',
            Longitud = '{longitud}',
            Actividad = '{actividad}',
            Descripcion = '{descripcion}'
            WHERE Cedula = '{cedula}'
            """)
            connection.commit()
            print('MODIFICACION COMPLETADA')
            input('Presiona ENTER para volver al MENU principal')
    else:
        print('El Usuario No Existe')
        input('Presiona ENTER para volver al MENU principal')
    pass


def eliminarMotor():
    print('---- ELIMINAR MOTOR -------')
    print('Lista de Motores Registrados')
    verMotores()
    cedula = input('Introduce la cedula del Motor que quiere Eliminar, o dejalo vacio para cancelar\n> ')
    if cedula == '':
        print('ELIMINACION CANCELADA')
        input('Presiona ENTER para volver al MENU principal')
    else:
        usuarioExiste = False
        for row in cursor.execute(f"SELECT Cedula FROM Motores WHERE Cedula = '{cedula}'"):
            if row:
                usuarioExiste = True
                pass
            pass

        if usuarioExiste:
            cursor.execute(f"DELETE FROM Motores WHERE Cedula = '{cedula}'")
            connection.commit()
            print('ELIMINACION COMPLETADA')
            input('Presiona ENTER para volver al MENU principal')
        else:
            print('El Usuario No Existe')
            input('Presiona ENTER para volver al MENU principal')
            pass
        pass
    pass

def exportarDatos():
    licencias = []
    for rows in cursor.execute('SELECT * FROM Motores'):
        licencia = f"""
            <div class="licencia">
            <div class="title">
                <h1>Licencia</h1>
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Coat_of_arms_of_the_Dominican_Republic.svg/1200px-Coat_of_arms_of_the_Dominican_Republic.svg.png"
                    alt="Escudo de Republica Dominicana">
            </div>
            <div class="datos">
                <div class="cedula">
                    <h4>Cedula:</h4> {rows[0]}
                </div>
                <div class="nombre">
                    <h4>Nombre:</h4> {rows[1]}
                </div>
                <div class="marca">
                    <h4>Marca:</h4> {rows[2]}
                </div>
                <div class="modelo">
                    <h4>Modelo:</h4> {rows[3]}
                </div>
                <div class="placa">
                    <h4>Placa:</h4> {rows[4]}
                </div>
                <div class="telefono">
                    <h4>Telefono:</h4> {rows[6]}
                </div>
                <div class="localizacion">
                    <h4>Latitud:</h4> {rows[8]}
                </div>
                <div class="localizacion">
                    <h4>longitud:</h4> {rows[9]}
                </div>
                <div class="direccion">
                    <h4>Direccion:</h4> {rows[7]}
                </div>
                <div class="actividad-descripcion">
                    <h4>Actividad y Descripci&oacute;n</h4> {rows[10]}, {rows[11]}
                </div>
            </div>
        </div>
        """

        licencias.append(licencia)
        pass

    todas_licencias = ''.join(licencias)
    html= (f"""
    <!DOCTYPE html>
    <html lang="es">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <title>Datos</title>
    </head>

    <body>
        <div class="container">
            #todas_licencias
        </div>
    </body>

    </html>
    """)

    html = html.replace('#todas_licencias', todas_licencias)

    f = open('data.html', 'w')
    f.write(html)
    f.close()
    webbrowser.open('data.html')
    pass
