"""
Módulo de utilidades y funciones auxiliares
Contiene funciones de uso general para el sistema de reservas
"""
import os
import json

def limpiarConsola():
    # Funciona en Windows, Linux y Mac
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux y Mac
        os.system('clear')

def getDatos():
    with open('data/usuarios.json', 'r') as archivo:
        USUARIOS = json.load(archivo)
    with open('data/horarios.json', 'r') as archivo:
        LISTA_HORARIOS = json.load(archivo)
    return USUARIOS, LISTA_HORARIOS

def guardarDatos(USUARIOS):
     with open('data/usuarios.json', 'w') as archivo:
                json.dump(USUARIOS, archivo, indent=4)

def getCapacidadMaxima():
    with open('data/capacidad_maxima.json', 'r') as archivo:
        CAPACIDAD_MAXIMA = json.load(archivo)
    return CAPACIDAD_MAXIMA