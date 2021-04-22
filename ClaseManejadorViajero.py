import csv
import os
from ClaseViajeroFrecuente import ViajeroFrecuente

class ManejadorViajero:

    def __init__(self):
        self.__listaViajeros = []

    def CrearLista(self):
        archivo = open('archivo.csv')
        reader = csv.reader(archivo, delimiter=',')

        for fila in reader:
            d1 = int(fila[0])
            d2 = int(fila[1])
            d3 = str(fila[2])
            d4 = str(fila[3])
            d5 = int(fila[4])
            Unviajero = ViajeroFrecuente(d1, d2, d3, d4, d5)
            self.AgregarViajero(Unviajero)

    def AgregarViajero(self, v1):
        self.__listaViajeros.append(v1)

    def BuscarViajero(self, v1):
        cont = 0
        aux = 0
        encontrado = 0
        UnViajero = ViajeroFrecuente()
        for UnViajero in self.__listaViajeros:
            if UnViajero.getNum() == int(v1):
                aux = cont
                cont = -1
                encontrado = 1
                print(f"El viajero {v1} fue encontrado con exito")
            if cont != -1:
                cont += 1
        if encontrado == 0:
            print(f"El viajero {v1} no fue encontrado")
            aux = "error"
        return aux

    def MostrarMillas(self, v1):
        print(f"Las millas del viajero suman un total de: {self.__listaViajeros[v1].cantidadTotaldeMillas()}")
        os.system("pause")

    def SumarMillas(self, v1):
        NuevasMillas = input("Ingrese cantidad de millas a agregar: ")
        self.__listaViajeros[v1].acumuladorMillas(NuevasMillas)
        print(f"Millas agregadas: {NuevasMillas}")
        print(f"Millas totales: {self.__listaViajeros[v1].cantidadTotaldeMillas()}")

    def RestarMillas(self, v1):
        MillasCanje = int(input("Ingrese cantidad de millas a ser canjeadas: "))
        self.__listaViajeros[v1].CanjearMillas(MillasCanje)
