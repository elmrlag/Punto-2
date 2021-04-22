from ClaseViajeroFrecuente import ViajeroFrecuente
from ClaseManejadorViajero import ManejadorViajero
import csv

def opcion0():
    print("Saliendo")

def opcion1():
    MV.MostrarMillas(posi)

def opcion2():
    MV.SumarMillas(posi)

def opcion3():
    MV.RestarMillas(posi)

switcher ={
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opcion incorrecta"))
    func()

if __name__=='__main__':
    bandera = False
    Viajero = ViajeroFrecuente()
    MV = ManejadorViajero()
    MV.CrearLista()

    print("Bienvenido")
    ViajeroNum = input("Ingrese numero de viajero: ")
    posi = MV.BuscarViajero(ViajeroNum)

    while not bandera:
        print("MENU DE OPCIONES")
        print("0 para salir")
        print("1 para Consultar Cantidad de Millas")
        print("2 para Acumular Millas")
        print("3 para Canjear Millas")
        opcion = int(input("Ingrese valor: "))
        switch(opcion)
        bandera = int(opcion) == 0