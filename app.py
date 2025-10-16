from constantes import USUARIOS, LISTA_HORARIOS
from registro import registrarUsuario
from reservas import *
from utilidades import limpiarConsola
import getpass

def main():
    #Comienzo del programa
    limpiarConsola()
    print("Bienvenido al sistema de reservas de turnos.")
    cuenta = input("Ya tienes una cuenta? (S/N): ")
    if (cuenta.lower() == "n"):
        limpiarConsola()
        registrarUsuario(USUARIOS)

    #login
    limpiarConsola()
    print("=== LOGIN ===")
    nombreUsuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    while nombreUsuario not in USUARIOS or USUARIOS[nombreUsuario]["contraseña"] != contraseña:
        print("Usuario o contraseña incorrectos. Intente nuevamente.")
        nombreUsuario = input("Ingrese su nombre de usuario: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")
    usuarioLogueado = USUARIOS[nombreUsuario]

    limpiarConsola()
    print(f"Bienvenido, {nombreUsuario}!")

    opcion = 0
    OPCION_SALIR=5 # por si añadimos mas opciones
    while opcion != OPCION_SALIR:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Reservar un horario")
        print("2. Ver horarios ocupados")
        print("3. Publicar una reserva")
        print("4. Unirse a una reserva publicada")
        print(f"{OPCION_SALIR}. Cancelar y salir")

        try:
            opcion = int(input(f"Elija una opción (1 - 2 - 3 - 4 - {OPCION_SALIR}): "))
        except ValueError:
            print("Debe ingresar un número válido.")
            opcion = 0
            continue

        if opcion == 1:
            limpiarConsola()
            reserva = reservar(LISTA_HORARIOS, USUARIOS)
            if reserva != "CANCELAR":
                USUARIOS[nombreUsuario]["reservas"].append(reserva)
                print("Reserva registrada correctamente!")
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == 2:
            limpiarConsola()
            deporte = input("Ingrese el deporte para ver las reservas (Futbol, Padel, Tenis): ")
            mostrarReservasOcupadas(USUARIOS, deporte)
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == 3:
            limpiarConsola()
            mostrarMisReservas(usuarioLogueado)
            publicarReserva(usuarioLogueado,nombreUsuario)
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == 4:
            limpiarConsola()
            unirseReserva(nombreUsuario,USUARIOS)
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == OPCION_SALIR:
            limpiarConsola()
            #estoy pensando aca deberia escribir en el archivo los cambios hechos en usuariologueado
            print("Adiós!")
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")
            limpiarConsola()

main()