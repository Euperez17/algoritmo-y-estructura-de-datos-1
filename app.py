from constantes import USUARIOS, LISTA_HORARIOS
from registro import registrarUsuario
from reservas import *
#from reservas import mostrarReservasOcupadas
#from reservas import mostrarMisReservas
import getpass

def main():
    #Comienzo del programa
    print("Bienvenido al sistema de reservas de turnos.")
    cuenta = input("Ya tienes una cuenta? (S/N): ")
    if (cuenta.lower() == "n"):
        registrarUsuario(USUARIOS)

    #login
    nombreUsuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    while nombreUsuario not in USUARIOS or USUARIOS[nombreUsuario]["contraseña"] != contraseña:
        print("Usuario o contraseña incorrectos. Intente nuevamente.")
        nombreUsuario = input("Ingrese su nombre de usuario: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")
    usuarioLogueado = USUARIOS[nombreUsuario]

    opcion = 0
    OPCION_SALIR=4 # por si añadimos mas opciones
    while opcion != OPCION_SALIR:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Reservar un horario")
        print("2. Ver horarios ocupados")
        print("3. Publicar una reserva")
        print("4. Cancelar y salir")

        opcion = int(input("Elija una opción (1 - 2 - 3 - 4): "))

        if opcion == 1:
            reserva = reservar(LISTA_HORARIOS, USUARIOS)
            if reserva != "CANCELAR":
                USUARIOS[nombreUsuario]["reservas"].append(reserva)
                print("Reserva registrada correctamente!")
            input("Presione Enter para continuar...")
        elif opcion == 2:
            deporte = input("Ingrese el deporte para ver las reservas (Futbol, Padel, Tenis): ")
            mostrarReservasOcupadas(USUARIOS, deporte)
            input("Presione Enter para continuar...")
        elif opcion == 3:
            mostrarMisReservas(usuarioLogueado)
            publicarReserva(usuarioLogueado,nombreUsuario)
            input("Presione Enter para continuar...")
        elif opcion == OPCION_SALIR:
            #estoy pensando aca deberia escribir en el archivo los cambios hechos en usuariologueado
            print("Adiós!")
        else:
            print("Opción no válida.")

main()