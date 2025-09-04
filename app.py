from constantes import DATOS, LISTA_HORARIOS
from registro import registrarUsuario
from reservas import reservar
import getpass

def main():
    #Comienzo del programa
    print("Bienvenido al sistema de reservas de turnos.")
    cuenta = input("Ya tienes una cuenta? (S/N)")
    if (cuenta == "N" or cuenta == "n"):
        registrarUsuario(DATOS)

    #login
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    while usuario not in [u[0] for u in DATOS] or contraseña not in [u[1] for u in DATOS]:
        print("Usuario o contraseña incorrectos. Intente nuevamente.")
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")

    #buscamos al usuario que se logueo y guardamos su indice
    indiceUsuario = -1
    i = 0
    while i < len(DATOS) and indiceUsuario == -1:
        if DATOS[i][0] == usuario:
            indiceUsuario = i
        i += 1

    #primera reserva, luego loop principal de flujo de sistema
    seleccion = reservar(LISTA_HORARIOS,DATOS)

    while seleccion != "CANCELAR":

        DATOS[indiceUsuario][2].append(seleccion)

        if seleccion != "CANCELAR":
            print("Reserva registrada correctamente!")
        seleccion=reservar(LISTA_HORARIOS,DATOS)

    print("adios!")

main()