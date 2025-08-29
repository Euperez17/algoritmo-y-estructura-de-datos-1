

def mostrarDisponibles(lista, reservas):
    print("Horarios disponibles: ")
    for i in lista:
        if i not in reservas:
            print(i, end="  |  ")
    print("")


def reservar(HORARIOS,reservas):
    mostrarDisponibles(LISTA_HORARIOS,horariosReservados)
    seleccion = input("Indique el horario que desea reservar o 'CANCELAR' para cancelar: ")
    while (seleccion not in HORARIOS or seleccion in reservas) and seleccion != "CANCELAR":
        print("Ese horario no esta disponible en este momento. Por favor, intenta de nuevo")
        mostrarDisponibles(HORARIOS,reservas)    
        seleccion = input("Indique el horario que desea reservar o 'CANCELAR' para cancelar: ")
    return seleccion

LISTA_HORARIOS = ["08:00", "09:30", "11:00", "12:30", "14:00", "15:30", "17:00", "18:30", "20:00"]

horariosReservados = []


print("Bienvenido al sistema de reservas de turnos.")




seleccion = reservar(LISTA_HORARIOS,horariosReservados)

while seleccion != "CANCELAR":
    
    horariosReservados.append(seleccion)
    print("DEBUG:", horariosReservados)
    if seleccion != "CANCELAR":
        print("Reserva registrada correctamente!")
    seleccion=reservar(LISTA_HORARIOS,horariosReservados)
    



print("adios!")