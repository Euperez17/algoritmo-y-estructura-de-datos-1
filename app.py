#from constantes import USUARIOS, LISTA_HORARIOS
import json
from registro import registrarUsuario
from reservas import *
from utilidades import limpiarConsola, getDatos,guardarDatos
import getpass

def main():
    #Comienzo del programa
    USUARIOS,LISTA_HORARIOS = getDatos() #carga los datos desde el archivo JSON
    limpiarConsola()
    print("Bienvenido al sistema de reservas de turnos.")
    cuenta = input("Ya tienes una cuenta? (S/N): ")
    if (cuenta.lower() == "n"):
        limpiarConsola()
        registrarUsuario(USUARIOS) #agrega un nuevo usuario al diccionario USUARIOS y guarda los datos en el archivo usuarios.json
        print("Usuario registrado exitosamente.")

    #login
    limpiarConsola()
    print("=== LOGIN ===")
    nombreUsuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    while nombreUsuario not in USUARIOS or USUARIOS[nombreUsuario]["contrasena"] != contraseña: #muy importante: JSON no entiende la ñ, asi que esta cambiado a contrasena dentro del diccionario
        print("Usuario o contraseña incorrectos. Intente nuevamente.")
        nombreUsuario = input("Ingrese su nombre de usuario: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")
    usuarioLogueado = USUARIOS[nombreUsuario] #obtenemos el diccionario del usuario logueado

    limpiarConsola()
    print(f"Bienvenido, {nombreUsuario}!") #damos la bienvenida al usuario

    opcion = 0
    OPCION_SALIR=6 #por si añadimos mas opciones
    while opcion != OPCION_SALIR:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Reservar un horario")
        print("2. Ver horarios ocupados")
        print("3. Publicar una reserva")
        print("4. Unirse a una reserva publicada")
        print("5. Confirmar pago de reserva")
        print(f"{OPCION_SALIR}. Cancelar y salir")

        try: #este try es para evitar que el programa falle si el usuario ingresa algo que no es un numero
            opcion = int(input(f"Elija una opción (1 - 2 - 3 - 4 - 5 - {OPCION_SALIR}): "))
        except ValueError:
            print("Debe ingresar un número válido.")
            opcion = 0
            continue

        if opcion == 1: #reservar un horario
            limpiarConsola()
            reserva = reservar(LISTA_HORARIOS, USUARIOS)
            if reserva != "CANCELAR":
                USUARIOS[nombreUsuario]["reservas"].append(reserva) #agregamos la reserva al usuario logueado
                print("Reserva registrada correctamente!")
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == 2: #ver horarios ocupados
            limpiarConsola()
            deporte = input("Ingrese el deporte para ver las reservas (Futbol, Padel, Tenis): ")
            mostrarReservasOcupadas(USUARIOS, deporte) #muestra las reservas ocupadas para el deporte seleccionado
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == 3: #publicar una reserva
            limpiarConsola()
            mostrarMisReservas(usuarioLogueado) #muestra las reservas del usuario logueado
            publicarReserva(usuarioLogueado,nombreUsuario) #publica una reserva privada del usuario logueado
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == 4: #unirse a una reserva publicada
            limpiarConsola()
            unirseReserva(nombreUsuario,USUARIOS) #permite al usuario logueado unirse a una reserva publica
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == 5: #confirmar pago de una reserva
            limpiarConsola()
            mostrarMisReservas(usuarioLogueado) #muestra las reservas del usuario logueado
            confirmarPagoReserva(usuarioLogueado) #marca una reserva como pagada
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == OPCION_SALIR: #salir del programa
            limpiarConsola()
            guardarDatos(USUARIOS) #guarda los datos en el archivo usuarios.json
            print("Adiós!")
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")
            limpiarConsola()

main()