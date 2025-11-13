#from constantes import USUARIOS, LISTA_HORARIOS
import json
from registro import registrarUsuario
from reservas import *
from utilidades import limpiarConsola, cargarDatosIniciales,guardarUsuarios
import getpass

"""
Sistema de reservas de canchas deportivas
Programa principal que gestiona el registro, login y reservas de usuarios
"""
def main():
    #Comienzo del programa
    USUARIOS,LISTA_HORARIOS = cargarDatosIniciales() #carga los datos desde el archivo JSON
    limpiarConsola()
    print("Bienvenido al sistema de reservas de turnos.")
    tieneCuenta = input("Ya tienes una cuenta? (S/N): ")
    if (tieneCuenta.lower() == "n"):
        limpiarConsola()
        registrarUsuario(USUARIOS) #agrega un nuevo usuario al diccionario USUARIOS
        guardarUsuarios(USUARIOS) #guarda el nuevo usuario en el archivo JSON
        print("Usuario registrado exitosamente.")

    #login
    limpiarConsola()
    print("=== LOGIN ===")
    nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
    contraseña = getpass.getpass("Ingrese su contraseña: ")

    # Buscar el usuario comparando en minusculas (case insensitive)
    nombreUsuarioReal = ""
    for usuario in USUARIOS:
        if usuario.lower() == nombreUsuario.lower():
            nombreUsuarioReal = usuario

    while nombreUsuarioReal == "" or USUARIOS[nombreUsuarioReal]["contrasena"] != contraseña: #muy importante: JSON no entiende la ñ, asi que esta cambiado a contrasena dentro del diccionario
        print("Usuario o contraseña incorrectos. Intente nuevamente.")
        nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
        contraseña = getpass.getpass("Ingrese su contraseña: ")
        # Buscar el usuario nuevamente
        nombreUsuarioReal = ""
        for usuario in USUARIOS:
            if usuario.lower() == nombreUsuario.lower():
                nombreUsuarioReal = usuario

    usuarioLogueado = USUARIOS[nombreUsuarioReal] #obtenemos el diccionario del usuario logueado
    nombreUsuario = nombreUsuarioReal #usamos el nombre real del usuario para las operaciones

    limpiarConsola()
    print(f"Bienvenido, {nombreUsuario}!") #damos la bienvenida al usuario

    opcion = 0
    OPCION_SALIR=5 #por si añadimos mas opciones
    while opcion != OPCION_SALIR:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Reservar un horario")
        print("2. Ver horarios ocupados")
        print("3. Publicar una reserva")
        print("4. Unirse a una reserva publicada")
        print(f"{OPCION_SALIR}. Cancelar y salir")

        try: #este try es para evitar que el programa falle si el usuario ingresa algo que no es un numero
            opcion = int(input(f"Elija una opción (1 - 2 - 3 - 4 - {OPCION_SALIR}): "))
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
            deporte = input("Ingrese el deporte para ver las reservas (Futbol, Padel, Tenis) o 'CANCELAR': ")
            if deporte.upper() != "CANCELAR":
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
        elif opcion == OPCION_SALIR: #salir del programa
            limpiarConsola()
            guardarUsuarios(USUARIOS) #guarda los datos en el archivo usuarios.json
            print("Adiós!")
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")
            limpiarConsola()

main()