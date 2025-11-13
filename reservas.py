"""
Módulo de gestión de reservas
Funciones para crear, visualizar y administrar reservas de canchas deportivas
"""
from datetime import datetime
#from constantes import CAPACIDAD_MAXIMA
from utilidades import getCapacidadMaxima

def buscarHorariosReservados(usuarios):
    """
    Busca todas las reservas realizadas por todos los usuarios.
    Devuelve: Lista con todas las reservas del sistema
    """
    return [reserva for usuario in usuarios.values() for reserva in usuario.get("reservas", [])] #lista de todas las reservas hechas por todos los usuarios

def horarioEstaOcupado(reservados, deporte, horario):
    """
    Verifica si un horario especifico esta ocupado para un deporte.
    Devuelve: True si el horario esta ocupado, False en caso contrario
    """
    for reserva in reservados:
        if reserva.get("Deporte", "") == deporte and reserva.get("Horario", "") == horario: #si el deporte y el horario coinciden
            return True
    return False

def mostrarReservasDisponibles(dictHorarios, dictUsuarios, deporte):
    """
    Muestra los horarios disponibles para un deporte segun la hora actual.
    """
    ahora = datetime.now() # fecha y hora actual
    hora_actual_str = ahora.strftime("%H:%M")
    print(f"\nHora actual: {hora_actual_str}") #muestra la hora actual
    print(f"Horarios disponibles para {deporte}:") #horarios disponibles para el deporte seleccionado según la hora actual

    reservados = buscarHorariosReservados(dictUsuarios) #obtenemos todas las reservas hechas por todos los usuarios

    # Crear conjunto de horarios ocupados para el deporte seleccionado
    horariosOcupados = {reserva["Horario"] for reserva in reservados if reserva["Deporte"] == deporte}

    # Convertir hora actual a minutos para comparacion correcta
    hora_partes = hora_actual_str.split(":")
    minutos_actuales = int(hora_partes[0]) * 60 + int(hora_partes[1])

    # Filtrar horarios disponibles
    disponibles = []
    for horario in dictHorarios[deporte]:
        if horario not in horariosOcupados:
            # Convertir horario a minutos para comparacion
            horario_partes = horario.split(":")
            minutos_horario = int(horario_partes[0]) * 60 + int(horario_partes[1])
            if minutos_horario > minutos_actuales: #si el horario es mayor a la hora actual
                disponibles.append(horario) #agregamos el horario a la lista de disponibles

    if disponibles:
        print("  |  ".join(disponibles)) #mostramos los horarios disponibles separados por |
    else:
        print("No hay horarios disponibles.")

def mostrarReservasOcupadas(dictUsuarios, deporteBuscar):
    """
    Muestra los horarios ocupados para un deporte especifico.
    """
    print(f"\nHorarios ocupados para {deporteBuscar}:")
    reservados = buscarHorariosReservados(dictUsuarios) #obtenemos todas las reservas hechas por todos los usuarios

    # Filtramos horarios ocupados
    ocupados = [reserva["Horario"] for reserva in reservados if reserva["Deporte"].lower() == deporteBuscar.lower()]

    if ocupados:
        print(" | ".join(ocupados))
    else:
        print("No hay horarios reservados todavía.")

def reservar(dictHorarios, dictUsuarios):
    """
    Permite al usuario reservar un horario para un deporte.
    Devuelve: Diccionario con la reserva creada o "CANCELAR" si se cancela
    """
    # Elegir deporte
    print("\nDeportes disponibles:")
    deportes = list(dictHorarios.keys()) #obtenemos la lista de deportes disponibles
    for deporte in deportes:
        print(f"- {deporte}") #printeamos los deportes del complejo
    deporteIngresado = input("Ingrese el deporte para ver los horarios o 'CANCELAR': ").strip()

    # Convertir deportes a minusculas para comparacion case insensitive
    deportesLower = [deporteDisponible.lower() for deporteDisponible in deportes]

    #mientras el deporte ingresado no esté en la lista de deportes disponibles
    while deporteIngresado.lower() not in deportesLower and deporteIngresado.upper() != "CANCELAR":
        print("Ese deporte no existe. Intente de nuevo.")
        deporteIngresado = input("Ingrese el deporte o 'CANCELAR': ").strip()

    if deporteIngresado.upper() == "CANCELAR":
        return "CANCELAR"

    # Encontrar el deporte original con mayusculas correctas
    for deporteOriginal in deportes:
        if deporteOriginal.lower() == deporteIngresado.lower():
            deporteIngresado = deporteOriginal
            break

    # Elegir horario
    mostrarReservasDisponibles(dictHorarios, dictUsuarios, deporteIngresado)
    seleccion = input("Indique el horario que desea reservar o 'CANCELAR': ")

    reservados = buscarHorariosReservados(dictUsuarios)

    # Usamos funcion auxiliar para verificar disponibilidad
    while (seleccion not in dictHorarios[deporteIngresado] or horarioEstaOcupado(reservados, deporteIngresado, seleccion)) and seleccion.upper() != "CANCELAR":
        print("Ese horario no está disponible. Intente de nuevo.")
        mostrarReservasDisponibles(dictHorarios, dictUsuarios, deporteIngresado)
        seleccion = input("Indique el horario que desea reservar o 'CANCELAR': ")

    if seleccion.upper() == "CANCELAR":
        return "CANCELAR"

    return {"Deporte":deporteIngresado,"Horario":seleccion,"Integrantes":"privado"} #al menos por ahora, es privada por defecto

def mostrarMisReservas(usuarioLogueado):
    """
    Muestra las reservas del usuario logueado.
    """
    reservas = usuarioLogueado.get("reservas", [])

    if not reservas:
        print("No tienes reservas actualmente.")
        return

    for reserva in reservas:
        integrantes = reserva.get("Integrantes", "privado")

        print(f"{reserva['Deporte']} - Horario: {reserva['Horario']} - ", end="")
        if integrantes != "privado":
            # Usamos join() para mostrar integrantes de forma mas clara
            print(f"Integrantes: {', '.join(integrantes)}")
        else:
            print("Privada")

def publicarReserva(usuarioLogueado, nombreUsuario):
    """
    Permite al usuario publicar una reserva privada para que otros se unan.
    """
    # Filtramos las reservas privadas del usuario
    reservas = usuarioLogueado.get("reservas", [])
    reservasPrivadas = [reserva for reserva in reservas if reserva.get("Integrantes") == "privado"]  #lista de reservas privadas

    if not reservasPrivadas:
        print("Ups! No tienes reservas privadas para publicar.")
        return

    print("\nTus reservas privadas:")
    for indice, reserva in enumerate(reservasPrivadas, start=1): #mostramos las reservas privadas con un indice
        print(f"{indice}. {reserva['Deporte']} - {reserva['Horario']}") #printeamos el indice, deporte y horario de la reserva privada

    seleccionInput = input("Seleccione el número de la reserva que desea publicar o '0' para cancelar: ")

    if seleccionInput == "0":
        print("Operación cancelada.")
        return
    try:
        seleccion = int(seleccionInput) - 1
        if seleccion < 0 or seleccion >= len(reservasPrivadas): #verificamos que la seleccion esté dentro del rango, sino, mostramos un error
            print("Selección inválida.")
            return
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    reservaSeleccionada = reservasPrivadas[seleccion]
    deporte = reservaSeleccionada["Deporte"]

    # Convertimos la reserva a publica
    reservaSeleccionada["Integrantes"] = [nombreUsuario]
    CAPACIDAD_MAXIMA = getCapacidadMaxima()
    capacidad = CAPACIDAD_MAXIMA.get(deporte, 0)  # Acceso seguro con valor por defecto
    reservaSeleccionada["CupoMaximo"] = capacidad
    print(f"\nReserva publicada! Otros usuarios pueden unirse hasta completar {capacidad} integrantes.")

def unirseReserva(nombreUsuario, usuarios):
    """
    Permite al usuario unirse a una reserva publica de otro usuario.
    """
    print("Reservas publicas")
    usuariosReservas = []  # Lista de tuplas (nombreUsuario, indiceReserva)
    contador = 0

    for nombreUsuarioPropietario, datosUsuario in usuarios.items(): 
        if nombreUsuarioPropietario != nombreUsuario:
            reservasUsuario = datosUsuario.get("reservas", []) 
            indiceReserva = 0

            for reserva in reservasUsuario:
                integrantes = reserva.get("Integrantes", "privado")
                # Mostrar solo reservas publicas de las que no es integrante
                if integrantes != "privado" and nombreUsuario not in integrantes:
                    listaIntegrantes = ', '.join(integrantes)
                    print(f"{contador + 1}. {reserva['Deporte']} a las {reserva['Horario']}. Integrantes: {listaIntegrantes}") #printeamos el indice, deporte, horario e integrantes de la reserva publicada
                    usuariosReservas.append((nombreUsuarioPropietario, indiceReserva))
                    contador += 1
                indiceReserva += 1
    
    if contador == 0:
        print("No hay reservas publicas!")
    else:
        while True: #Tecnica para emular un do-while (no le va a gustar a la profe)
            seleccionInput = input("Seleccione la reserva a la que se quiere unir o '0' para cancelar: ")

            if seleccionInput == "0":
                print("Operación cancelada.")
                return

            try:
                seleccion = int(seleccionInput) - 1
                if seleccion >= contador or seleccion < 0: #verificamos que la seleccion esté dentro del rango
                    print("Reserva fuera de rango. Intente de nuevo")
                else:
                    break
            except ValueError:
                print("Debe ingresar un número válido.")

        usuarioSeleccionado, indiceReservaSeleccionada = usuariosReservas[seleccion]
        reservaSeleccionada = usuarios[usuarioSeleccionado]["reservas"][indiceReservaSeleccionada]

        # Verificar si la reserva tiene CupoMaximo, si no asignarlo según el deporte
        cupoMaximo = reservaSeleccionada.get("CupoMaximo", None)
        if cupoMaximo is None: #si no tiene cupoMaximo asignado
            deporte = reservaSeleccionada.get("Deporte", "")
            CAPACIDAD_MAXIMA = getCapacidadMaxima()
            cupoMaximo = CAPACIDAD_MAXIMA.get(deporte, 0) #obtenemos la capacidad maxima del deporte
            if cupoMaximo > 0:
                reservaSeleccionada["CupoMaximo"] = cupoMaximo
                print(f"Advertencia: Se asignó cupo máximo de {cupoMaximo} a esta reserva de {deporte}.")
            else:
                print(f"Error: No se pudo determinar la capacidad para el deporte '{deporte}'.")
                return

        integrantesActuales = len(reservaSeleccionada["Integrantes"]) #cantidad de integrantes actuales en la reserva

        if integrantesActuales >= cupoMaximo:
            print(f"Lo siento, la reserva ya alcanzó su capacidad máxima de {cupoMaximo} integrantes.")
        else:
            reservaSeleccionada["Integrantes"].append(nombreUsuario)
            print(f"Reserva actualizada correctamente! Ahora son {integrantesActuales + 1}/{cupoMaximo} integrantes.")
