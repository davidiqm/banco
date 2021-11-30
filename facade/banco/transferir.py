from os import system

from db.connection import DataBase
from singleton.usuario import Usuario


class Transferir:
    def transferir(self):
        system('cls')
        usuario = Usuario()
        conn = DataBase()

        print('Para la transferencia bancaria ingrese los datos')

        numCuenta = int(input('Numero de cuenta:'))
        cantidad = int(input('Cantidad:'))

        try:
            nuevoBalance = usuario.getBalance() - cantidad

            conn.transferenciaBancaria(numCuenta, cantidad, nuevoBalance)
            usuario.setBalance(nuevoBalance)

        except:
            print('Ha ocurrido un error')
