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