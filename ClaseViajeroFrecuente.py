class ViajeroFrecuente:
    __NumViajero = 0
    __DNI = 0
    __Nombre = 0
    __Apellido = 0
    __MillasAcum = 0

    def __init__(self, v1 = 0, v2 = 0, v3 = "Ejem", v4 = "Plo", v5 = 0):
        self.__NumViajero = v1
        self.__DNI = v2
        self.__Nombre = v3
        self.__Apellido = v4
        self.__MillasAcum = v5

    def getNum(self):
        return(self.__NumViajero)

    def cantidadTotaldeMillas(self):
        return(self.__MillasAcum)

    def acumuladorMillas(self, v1):
        self.__MillasAcum = self.__MillasAcum + int(v1)

    def CanjearMillas(self, v1):
        if (self.__MillasAcum > int(v1)):
            aux = self.__MillasAcum
            self.__MillasAcum = self.__MillasAcum - v1
            print("Canje de millas realizado")
            print(f"Cantidad anterior de millas: {aux}")
            print(f"Cantidad de millas a canjeadas: {v1}")
            print(f"Cantidad de millas actuales: {self.__MillasAcum}")
        else:
            print("ERROR en el canje de millas")