from os import system

from db.connection import DataBase
from singleton.usuario import Usuario


class Interbancario:
    def transferir(self):
        system('cls')
        usuario = Usuario()
        conn = DataBase()

        print('Para la transferencia interbancaria ingrese los datos')

        clabe = int(input('CLABE:'))
        cantidad = int(input('Cantidad:'))

        try:
            nuevoBalance = usuario.getBalance() - cantidad

            conn.transferenciaInterbancaria(nuevoBalance)
            usuario.setBalance(nuevoBalance)

            input('Transferencia interbancaria con exito')
        except:
            print('Ha ocurrido un error')
