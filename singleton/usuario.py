from os import name


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Usuario(metaclass=SingletonMeta):
    def __init__(self, idUser, numCuenta, nombre, balance):
        self._id = idUser
        self._numCuenta = numCuenta
        self._nombre = nombre
        self._balance = balance

    def getId(self):
        return self._id

    def getNombre(self):
        return self._nombre

    def getBalance(self):
        return self._balance

    def setBalance(self, balance):
        self._balance = balance
