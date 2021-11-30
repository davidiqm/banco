from os import system

from db.connection import DataBase
from facade.framework import Framework

if __name__ == "__main__":
    system('cls')
    print('Bienvenido. Ingrese sus datos para iniciar sesion\n')

    cuenta = int(input('Cuenta: '))
    contra = input('Contraseña: ')

    resultado = DataBase().iniciarSesion(cuenta, contra)

    if resultado:
        Framework().menu()
    else:
        print('Credenciales incorrectas')
