from datetime import datetime
#from constantes import CAPACIDAD_MAXIMA
from utilidades import getCapacidadMaxima

def buscarHorariosReservados(usuarios):
    return [reserva for usuario in usuarios.values() for reserva in usuario["reservas"]]

def horarioEstaOcupado(reservados, deporte, horario):
    # Verifica si un horario especifico esta ocupado para un deporte
    for reserva in reservados:
        if reserva["Deporte"] == deporte and reserva["Horario"] == horario:
            return True
    return False

def mostrarReservasDisponibles(lista, datos, deporte):
    ahora = datetime.now() # fecha y hora actual
    hora_actual_str = ahora.strftime("%H:%M")
    print(f"\nHora actual: {hora_actual_str}")
    print(f"Horarios disponibles para {deporte}:")

    reservados = buscarHorariosReservados(datos)

    # Crear conjunto de horarios ocupados
    horariosOcupados = {reserva["Horario"] for reserva in reservados if reserva["Deporte"] == deporte}

    # Convertir hora actual a minutos para comparacion correcta
    hora_partes = hora_actual_str.split(":")
    minutos_actuales = int(hora_partes[0]) * 60 + int(hora_partes[1])

    # Filtrar horarios disponibles
    disponibles = []
    for horario in lista[deporte]:
        if horario not in horariosOcupados:
            # Convertir horario a minutos para comparacion
            horario_partes = horario.split(":")
            minutos_horario = int(horario_partes[0]) * 60 + int(horario_partes[1])
            if minutos_horario > minutos_actuales:
                disponibles.append(horario)

    if disponibles:
        print("  |  ".join(disponibles))
    else:
        print("No hay horarios disponibles.")

def mostrarReservasOcupadas(DATOS, deporteBuscar):
    print(f"\nHorarios ocupados para {deporteBuscar}:")
    reservados = buscarHorariosReservados(DATOS)

    # Filtramos horarios ocupados
    ocupados = [reserva["Horario"] for reserva in reservados if reserva["Deporte"].lower() == deporteBuscar.lower()]

    if ocupados:
        print(" | ".join(ocupados))
    else:
        print("No hay horarios reservados todavía.")

def reservar(HORARIOS, datos):
    # Elegir deporte
    print("\nDeportes disponibles:")
    deportes = list(HORARIOS.keys())
    for deporte in deportes:
        print(f"- {deporte}")
    deporteIngresado = input("Ingrese el deporte para ver los horarios o 'CANCELAR': ").strip()

    # Convertir deportes a minusculas para comparacion case insensitive
    deportesLower = [deporteDisponible.lower() for deporteDisponible in deportes]

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

    deporte = deporteIngresado

    # Elegir horario
    mostrarReservasDisponibles(HORARIOS, datos, deporte)
    seleccion = input("Indique el horario que desea reservar o 'CANCELAR': ")

    reservados = buscarHorariosReservados(datos)

    # Usamos funcion auxiliar para verificar disponibilidad
    while (seleccion not in HORARIOS[deporte] or horarioEstaOcupado(reservados, deporte, seleccion)) and seleccion.upper() != "CANCELAR":
        print("Ese horario no está disponible. Intente de nuevo.")
        mostrarReservasDisponibles(HORARIOS, datos, deporte)
        seleccion = input("Indique el horario que desea reservar o 'CANCELAR': ")

    if seleccion.upper() == "CANCELAR":
        return "CANCELAR"

    return {"Deporte":deporte,"Horario":seleccion,"Integrantes":"privado"} #al menos por ahora, es privada por defecto

# Devuelve las reservas que tiene el usuario
def mostrarMisReservas(usuarioLogueado):
    reservas = usuarioLogueado.get("reservas", [])

    if not reservas:
        print("No tienes reservas actualmente.")
        return

    for reserva in reservas:
        integrantes = reserva.get("Integrantes", "privado")

        print(f"{reserva['Deporte']} - Horario: {reserva['Horario']} - ", end="")
        if integrantes != "privado":
            # Usar join() para mostrar integrantes de forma mas clara
            print(f"Integrantes: {', '.join(integrantes)}")
        else:
            print("Privada")

def publicarReserva(usuarioLogueado, nombreUsuario):
    # Filtrar las reservas privadas del usuario
    reservas = usuarioLogueado.get("reservas", [])
    reservasPrivadas = [reserva for reserva in reservas if reserva.get("Integrantes") == "privado"]

    if not reservasPrivadas:
        print("Ups! No tienes reservas privadas para publicar.")
        return

    print("\nTus reservas privadas:")
    for indice, reserva in enumerate(reservasPrivadas, start=1):
        print(f"{indice}. {reserva['Deporte']} - {reserva['Horario']}")

    try:
        seleccion = int(input("Seleccione el número de la reserva que desea publicar: ")) - 1
        if seleccion < 0 or seleccion >= len(reservasPrivadas):
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
                    print(f"{contador + 1}. {reserva['Deporte']} a las {reserva['Horario']}. Integrantes: {listaIntegrantes}")
                    usuariosReservas.append((nombreUsuarioPropietario, indiceReserva))
                    contador += 1
                indiceReserva += 1
    
    if contador == 0:
        print("No hay reservas publicas!")
    else:

        while True:  # Tecnica para emular un do-while
            try:
                seleccion = int(input("Seleccione la reserva a la que se quiere unir: ")) - 1
                if seleccion >= contador or seleccion < 0:
                    print("Reserva fuera de rango. Intente de nuevo")
                else:
                    break
            except ValueError:
                print("Debe ingresar un número válido.")

        usuarioSeleccionado, indiceReservaSeleccionada = usuariosReservas[seleccion]
        reservaSeleccionada = usuarios[usuarioSeleccionado]["reservas"][indiceReservaSeleccionada]

        # Verificar si la reserva tiene CupoMaximo, si no asignarlo según el deporte
        cupoMaximo = reservaSeleccionada.get("CupoMaximo", None)
        if cupoMaximo is None:
            deporte = reservaSeleccionada.get("Deporte", "")
            CAPACIDAD_MAXIMA = getCapacidadMaxima()
            cupoMaximo = CAPACIDAD_MAXIMA.get(deporte, 0)
            if cupoMaximo > 0:
                reservaSeleccionada["CupoMaximo"] = cupoMaximo
                print(f"Advertencia: Se asignó cupo máximo de {cupoMaximo} a esta reserva de {deporte}.")
            else:
                print(f"Error: No se pudo determinar la capacidad para el deporte '{deporte}'.")
                return

        integrantesActuales = len(reservaSeleccionada["Integrantes"])

        if integrantesActuales >= cupoMaximo:
            print(f"Lo siento, la reserva ya alcanzó su capacidad máxima de {cupoMaximo} integrantes.")
        else:
            reservaSeleccionada["Integrantes"].append(nombreUsuario)
            print(f"Reserva actualizada correctamente! Ahora son {integrantesActuales + 1}/{cupoMaximo} integrantes.")
    
