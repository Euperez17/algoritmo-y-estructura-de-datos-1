from constantes import USUARIOS, LISTA_HORARIOS
from registro import registrarUsuario
from reservas import reservar
from reservas import mostrarReservasOcupadas
import getpass

def main():
    #Comienzo del programa
    print("Bienvenido al sistema de reservas de turnos.")
    cuenta = input("Ya tienes una cuenta? (S/N): ")
    if (cuenta.lower() == "n"):
        registrarUsuario(USUARIOS)

    #login
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    while usuario not in USUARIOS or USUARIOS[usuario]["contraseña"] != contraseña:
        print("Usuario o contraseña incorrectos. Intente nuevamente.")
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")

    opcion = 0
    while opcion != 3:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Reservar un horario")
        print("2. Ver horarios ocupados")
        print("3. Cancelar y salir")

        opcion = int(input("Elija una opción (1 - 2 - 3): "))

        if opcion == 1:
            seleccion = reservar(LISTA_HORARIOS, USUARIOS)
            if seleccion != "CANCELAR":
                USUARIOS[usuario]["reservas"].append(seleccion)
                print("Reserva registrada correctamente!")
        elif opcion == 2:
            deporte = input("Ingrese el deporte para ver las reservas (Futbol, Padel, Tenis): ")
            mostrarReservasOcupadas(USUARIOS, deporte)
        elif opcion == 3:
            print("Adiós!")
        else:
            print("Opción no válida.")

main()