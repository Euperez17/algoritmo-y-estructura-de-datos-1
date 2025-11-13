"""
Modulo de utilidades y funciones auxiliares
Contiene funciones de uso general para el sistema de reservas
"""
import os
import json

def limpiarConsola():
    """
    Limpia la consola del terminal.
    Funciona en Windows, Linux y Mac.
    """
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux y Mac
        os.system('clear')

def cargarDatosIniciales():
    """
    Carga los datos de usuarios y horarios desde archivos JSON.
    Devuelve: tupla: (USUARIOS, LISTA_HORARIOS) - Diccionarios con datos del sistema
    """
    import json

    # Cargar usuarios
    try:
        with open('data/usuarios.json', 'r') as archivo:
            USUARIOS = json.load(archivo)
    except:
        print("No se pudo abrir usuarios.json, se crea vacío.")
        USUARIOS = {}

    # Cargar horarios
    try:
        with open('data/horarios.json', 'r') as archivo:
            LISTA_HORARIOS = json.load(archivo)
    except:
        print("No se pudo abrir horarios.json, el programa termina.")
        exit()

    return USUARIOS, LISTA_HORARIOS

def guardarUsuarios(USUARIOS):
     """
    Guarda los datos de usuarios en el archivo JSON.

    Parametros:
        USUARIOS (dict): Diccionario con informacion de todos los usuarios
    """
     try:
        with open('data/usuarios.json', 'w') as archivo:
            json.dump(USUARIOS, archivo, indent=4)
     except:
        print("Error al guardar usuarios.json")
        print("Los cambios no se han guardado.")

def getCapacidadMaxima():
    """
    Carga la capacidad maxima de jugadores por deporte desde archivo JSON.

    Retorna:
        dict: Diccionario con capacidad maxima por deporte
    """
    try:
        with open('data/capacidad_maxima.json', 'r') as archivo:
            CAPACIDAD_MAXIMA = json.load(archivo)
        return CAPACIDAD_MAXIMA
    except:
        print("Usando capacidades por defecto.")
        return {"Futbol": 22, "Padel": 4, "Tenis": 4}