"""
Módulo de utilidades y funciones auxiliares
Contiene funciones de uso general para el sistema de reservas
"""
import os

def limpiarConsola():
    # Funciona en Windows, Linux y Mac
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux y Mac
        os.system('clear')
