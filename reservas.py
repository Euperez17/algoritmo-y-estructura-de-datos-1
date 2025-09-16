from datetime import datetime

def buscarHorariosReservados(datos):
    # lista de listas: Devuelve [[deporte, horario], ...]
    return [reserva for usuario in datos for reserva in usuario[2]]

def mostrarReservasDisponibles(lista, datos, deporte):
    ahora = datetime.now() # fecha y hora actual
    hora_actual = ahora.strftime("%H:%M")
    print(f"\nHora actual: {hora_actual}")
    print(f"Horarios disponibles para {deporte}:")

    reservados = buscarHorariosReservados(datos)

    # filtramos solo los horarios disponibles
    disponibles = list(filter(lambda h: [deporte, h] not in reservados and h > hora_actual, lista[deporte]))

    for horario in disponibles:
        print(horario, end="  |  ")
    print("")

def reservar(HORARIOS, datos):
    # Elegir deporte
    print("\nDeportes disponibles:")
    for dep in HORARIOS.keys():
        print(f"- {dep}")
    deporte = input("Ingrese el deporte para ver los horarios o 'CANCELAR': ")

    while deporte not in HORARIOS and deporte != "CANCELAR":
        print("Ese deporte no existe. Intente de nuevo.")
        deporte = input("Ingrese el deporte o 'CANCELAR': ")

    if deporte == "CANCELAR":
        return "CANCELAR"

    # Elegir horario
    mostrarReservasDisponibles(HORARIOS, datos, deporte)
    seleccion = input("Indique el horario que desea reservar o 'CANCELAR': ")

    reservados = buscarHorariosReservados(datos)
    while (seleccion not in HORARIOS[deporte] or [deporte, seleccion] in reservados) and seleccion != "CANCELAR":
        print("Ese horario no está disponible. Intente de nuevo.")
        mostrarReservasDisponibles(HORARIOS, datos, deporte)
        seleccion = input("Indique el horario que desea reservar o 'CANCELAR': ")

    if seleccion == "CANCELAR":
        return "CANCELAR"

    return [deporte, seleccion]
