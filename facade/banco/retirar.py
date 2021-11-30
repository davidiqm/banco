from os import system

from db.connection import DataBase
from singleton.usuario import Usuario


class Retirar:
    def retirar(self):
        system('cls')
        usuario = Usuario()
        conn = DataBase()

        print('Para el ingrese los datos')

        cantidad = int(input('Cantidad:'))

        try:
            nuevoBalance = usuario.getBalance() - cantidad

            conn.retirarDinero(nuevoBalance)
            usuario.setBalance(nuevoBalance)

            input('Retiro realizado con exito')
        except:
            print('Ha ocurrido un error')
