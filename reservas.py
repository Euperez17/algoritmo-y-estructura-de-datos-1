from datetime import datetime

def buscarHorariosReservados(datos):
    horariosReservados = []
    for usuario in datos:
        horariosReservados.extend(usuario[2])
    return horariosReservados

def mostrarReservasDisponibles(lista, datos):
    ahora = datetime.now() #fecha y hora actual
    hora_actual = ahora.strftime("%H:%M")
    print("\nHora actual: ",hora_actual)
    print("Horarios disponibles: ")

    reservados = buscarHorariosReservados(datos)

    for horario in lista:
        #Si el horario no esta reservado y si el horario es > a la hora actual, lo muestra
        if horario not in reservados and horario > hora_actual:
            print(horario, end="  |  ")
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