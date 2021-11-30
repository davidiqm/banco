import json

from singleton.usuario import Usuario


class DataBase:
    # Al iniciar sesion, se crea el Singleton del usuario, quien es el
    # objeto a través del que se mueve el sistema
    def iniciarSesion(self, numCuenta, contrasena) -> bool:
        f = open('db/users.json')
        data = json.load(f)

        for i in data:
            if i["numCuenta"] == numCuenta and i["contrasena"] == contrasena:

                # Creacion de usuario
                usuario = Usuario(i["id"], i["numCuenta"],
                                  i["nombre"], i["balance"])

                f.close()

                return True

        f.close()
        return False

    # Metodo para sacar dinero del sistema, ya sea para transferencia
    # interbancaria o retiro, modificando el json
    def retirarDinero(self, cantidad):
        f = open('db/users.json')
        data = json.load(f)
        f.close()

        usuario = Usuario()

        for i in data:
            if i["id"] == usuario.getId():
                i["balance"] = cantidad
                input('Transferencia realizada con exito')

        f = open('db/users.json', 'w')
        json.dump(data, f)
        f.close()

    # Metodo para transferir dinero de una cuenta a otra, modificando los
    # valores dentro del json
    def transferenciaBancaria(self, numCuenta, cantidad, nuevoBalance):
        f = open('db/users.json')
        data = json.load(f)
        f.close()

        usuario = Usuario()

        for i in data:
            if i["id"] == usuario.getId():
                i["balance"] = nuevoBalance

            if i["numCuenta"] == numCuenta:
                temp = i["balance"] + cantidad
                i["balance"] = temp
                input('Transferencia realizada con exito')

        f = open('db/users.json', 'w')
        json.dump(data, f)
        f.close()

    # Metodo para
    def transferenciaInterbancaria(self, cantidad):
        f = open('db/users.json')
        data = json.load(f)
        f.close()

        usuario = Usuario()

        for i in data:
            if i["id"] == usuario.getId():
                i["balance"] = cantidad
                input('Transferencia realizada con exito')

        f = open('db/users.json', 'w')
        json.dump(data, f)
        f.close()
