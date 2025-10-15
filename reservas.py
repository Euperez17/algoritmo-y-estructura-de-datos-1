from datetime import datetime
def buscarHorariosReservados(usuarios):
    
    return [reserva for usuario in usuarios.values() for reserva in usuario["reservas"]]

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

def mostrarReservasOcupadas(DATOS, deporteBuscar):
    print(f"\nHorarios ocupados para {deporteBuscar}:")
    reservados = buscarHorariosReservados(DATOS)
    #ocupados = [horario for deporte, horario in reservados if deporte == deporteBuscar] #h = horario, d = deporte -> chequea que horarios están ocupados por cada deporte
    ocupados=[] #aca podriamos añadir que muestre separado las reservas publicas, o ponerlo en otro lado para poder sumarse a la reserva
    for i in reservados:
        if i["Deporte"].lower()==deporteBuscar.lower():
            ocupados.append(i["Horario"])

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

    return {"Deporte":deporte,"Horario":seleccion,"Integrantes":"privado"} #al menos por ahora, es privada por defecto

def mostrarMisReservas(usuarioLogueado): #devuelve las reservas que tiene el usuario
    reservas=usuarioLogueado["reservas"]
    for reserva in usuarioLogueado["reservas"]:
        integrantes = reserva["Integrantes"]

        print(f"{reserva['Deporte']} - Horario: {reserva['Horario']} - ",end="")
        if integrantes!="privado":
            print(f"Integrantes: {[i for i in integrantes]}")
        else:
            print("Privada")

def publicarReserva(usuarioLogueado,nombreUsuario): #permite al usuario publicar una reserva privada que haya hecho 
    #hacer esta funcion me hace soñar con un menu dropdown 

    deportesConReservaPrivada = [reserva["Deporte"] for reserva in usuarioLogueado["reservas"] if reserva["Integrantes"]=="privado"]
    if len(deportesConReservaPrivada)<1:
        print("Ups! No tienes reservas privadas!") # es una MUY mala forma de chequear si no tiene reservas privadas jajajaja
        return #esto me da arcadas
    deporte = input("Indique deporte de la reserva: ")

    while deporte not in deportesConReservaPrivada:
        print("No tienes reservas privadas para ese deporte")
        deporte = input("Indique deporte de la reserva: ")
        

    reservasDeporte = [reserva for reserva in usuarioLogueado["reservas"] if reserva["Deporte"].lower() == deporte.lower()]
    horario = input("Indique horario de la reserva: ")
    
    reservaSeleccionada=None
    for reserva in reservasDeporte:
        if reserva["Horario"]==horario:
            reservaSeleccionada=reserva
            break

    while not reservaSeleccionada:
        print("No tienes una reserva privada para ese horario.")
        horario = input("Indique horario de la reserva: ")
        reservaSeleccionada=None
        for reserva in reservasDeporte:
            if reserva["Horario"]==horario:
                reservaSeleccionada=reserva
                break

    reservaSeleccionada["Integrantes"]=[nombreUsuario]
    print("Reserva publicada! Otros usuarios pueden unirse a tu reserva ahora.")

def unirseReserva(nombreUsuario,usuarios):
    print("Reservas publicas")
    usuariosReservas = [] #es ocmo una lista paralela al i, medio raro jiji
    i=0
    for nombre, data in usuarios.items():
        if nombre != nombreUsuario:
            for reserva in data["reservas"]:
                indiceReserva = 0 #contador interno
                if reserva["Integrantes"]!="privado" and nombreUsuario not in reserva["Integrantes"]: #se pone un poco confuso esto, pero basicamente muestra las reservas publicas de las que no es integrante
                    print(f"{i+1}. {reserva['Deporte']} a las {reserva['Horario']}. Integrantes: {[integrante for integrante in reserva['Integrantes']]}")
                    usuariosReservas.append((nombre,indiceReserva))
                    i+=1
                    indiceReserva+=1
    
    if i==0:
        print("No hay reservas publicas!")
    else:
        
        while True: #nueva tecinca para emular un do while
            seleccion = int(input("Seleccione la reserva a la que se quiere unir: "))-1 #-1 para traducirlo a indice de la lista
            if seleccion>i or seleccion<0:
                print("Reserva fuera de rango. Intente de nuevo")
            else: break

        usuarioseleccionado, indiceReservaSeleccionada = usuariosReservas[seleccion]
        usuarios[usuarioseleccionado]["reservas"][indiceReservaSeleccionada]["Integrantes"].append(nombreUsuario)
        print("Reserva actualizada correctamente!")
    
