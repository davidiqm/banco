from os import system

from facade.banco.retirar import Retirar
from facade.banco.transferir import Transferir
from facade.interbancario.interbancario import Interbancario
from singleton.usuario import Usuario


class Framework:
    def clearScreen(self):
        system('cls')

    def menu(self):
        usuario = Usuario()

        while True:
            self.clearScreen()
            print('Bienvenido, {}\nTu saldo es de: {}\n'.format(
                usuario.getNombre(), usuario.getBalance()))

            opcion = int(input('Menu:\n1. Transferir\n'
                               + '2. Retirar\n'
                               + '3. Transferencia interbancaria\n'
                               + '4. Salir\n'
                               + 'Opcion: '
                               ))

            if opcion == 1:
                Transferir().transferir()
            elif opcion == 2:
                Retirar().retirar()
            elif opcion == 3:
                Interbancario().transferir()
            else:
                break
