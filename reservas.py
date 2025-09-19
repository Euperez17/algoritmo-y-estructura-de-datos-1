from datetime import datetime
def buscarHorariosReservados(datos):
    # lista de listas: Devuelve [[deporte, horario], ...]
    return [reserva for usuario in datos.values() for reserva in usuario["reservas"]]

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

def mostrarReservasOcupadas(DATOS, deporte):
    print(f"\nHorarios ocupados para {deporte}:")
    reservados = buscarHorariosReservados(DATOS)
    ocupados = [h for d, h in reservados if d == deporte] #h = horario, d = deporte -> chequea que horarios están ocupados por cada deporte

    if not ocupados:
        print("No hay horarios reservados todavía.")
    else:
        for h in ocupados:
            print(h, end=" | ") 
    print("")

def reservar(HORARIOS, datos):
    # Elegir deporte
    print("\nDeportes disponibles:")
    deportes = list(HORARIOS.keys())
    for dep in deportes:
        print(f"- {dep}")
    deporte = input("Ingrese el deporte para ver los horarios o 'CANCELAR': ")


    while deporte not in deportes and deporte.upper() != "CANCELAR":
        print("Ese deporte no existe. Intente de nuevo.")
        deporte = input("Ingrese el deporte o 'CANCELAR': ")

    if deporte.upper() == "CANCELAR":
        return "CANCELAR"

    # Elegir horario
    mostrarReservasDisponibles(HORARIOS, datos, deporte)
    seleccion = input("Indique el horario que desea reservar o 'CANCELAR': ")

    reservados = buscarHorariosReservados(datos)
    while (seleccion not in HORARIOS[deporte] or [deporte, seleccion] in reservados) and seleccion.upper() != "CANCELAR":
        print("Ese horario no está disponible. Intente de nuevo.")
        mostrarReservasDisponibles(HORARIOS, datos, deporte)
        seleccion = input("Indique el horario que desea reservar o 'CANCELAR': ")

    if seleccion.upper() == "CANCELAR":
        return "CANCELAR"

    return [deporte, seleccion]
