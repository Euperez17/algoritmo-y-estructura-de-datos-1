import getpass

#hasta que aprendamos a usar archivos, hardcodeamos esta matriz para el login
DATOS = [] #estructura: nombre, contraseña, reservas hechas

DATOS.append(["dante", "1234", ["08:00"]])
DATOS.append(["augus", "5678", []])
# Constante de lista de horarios posibles
LISTA_HORARIOS = ["08:00", "09:30", "11:00", "12:30", "14:00", "15:30", "17:00", "18:30", "20:00"]

def buscarHorariosReservados(datos):
    horariosReservados = []
    for usuario in datos:
        horariosReservados.extend(usuario[2])
    return horariosReservados

def mostrarReservasDisponibles(lista, datos):
    print("Horarios disponibles: ")
    reservados = buscarHorariosReservados(datos)

    for i in lista:
        if i not in reservados:
            print(i, end="  |  ")
    print("")


def reservar(HORARIOS,datos):
    mostrarReservasDisponibles(HORARIOS,datos)
    seleccion = input("Indique el horario que desea reservar o 'CANCELAR' para cancelar: ")
    reservados = buscarHorariosReservados(datos)
    while (seleccion not in HORARIOS or seleccion in reservados) and seleccion != "CANCELAR":
        print("Ese horario no esta disponible en este momento. Por favor, intenta de nuevo")
        mostrarReservasDisponibles(HORARIOS,datos)
        seleccion = input("Indique el horario que desea reservar o 'CANCELAR' para cancelar: ")
    return seleccion

def registrarUsuario(datos):
        print("")
        print("Registro de usuario")

        usuario = input("Ingrese un nombre de usuario: ")
        while usuario in [u[0] for u in datos]:
            print("El nombre de usuario ya existe. Por favor, elige otro.")
            usuario = input("Ingrese un nombre de usuario: ")

        contraseña = getpass.getpass("Ingrese una contraseña segura: ") #estaria bueno que la contraseña no se muestre - tambien se puede agregar seguridad en un futuro
        datos.append([usuario, contraseña, []])
        print("Cuenta creada exitosamente!")
    

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