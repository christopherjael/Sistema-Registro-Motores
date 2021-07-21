from functions import *
from createDB import *
import time

createDB()
limpiar()
while True:
    print('Bienevenido/da a el Sistema de Registro de Motores')
    print('------ MENU ------')
    print('1. Registrar Motor')
    print('2. Modificar Registro')
    print('3. Eliminar Registro')
    print('4. Ver ubicación de los motores en el Mapa')
    print('5. Exportar datos')
    print('6. Salir del programa\n ')
    op = int(input('Introduce una opción\n> '))

    if op == 1:
        registrarMotor()
        limpiar()
    elif op == 2:
        modificarMotor()
        limpiar()
    elif op == 3:
        eliminarMotor()
        limpiar()
    elif op == 4:
        verMotoresMapa()
        limpiar()
    elif op == 5:
        exportarDatos()
        limpiar()
    elif op == 6:
        print('Saliendo del programa....')
        time.sleep(1)
        break
    else:
        input('La opcion no existe')
        limpiar()

