#from constantes import USUARIOS, LISTA_HORARIOS
import json
from registro import registrarUsuario
from reservas import *
from utilidades import limpiarConsola, cargarDatosIniciales,guardarUsuarios
import getpass

"""
Sistema de reservas de canchas deportivas
Programa principal que gestiona el registro, login y reservas de usuarios
"""
def main():
    USUARIOS, LISTA_HORARIOS = cargarDatosIniciales()
    nombreUsuarioReal = None # Guardará los datos del usuario logueado

    while nombreUsuarioReal is None: # Bucle principal: se repite hasta que el login sea exitoso
        limpiarConsola()
        print("Bienvenido al sistema de reservas de turnos.")
        print("-" * 30)
        
        tieneCuenta = input("Ya tenés una cuenta? (S/N): ")
        while tieneCuenta.lower() not in ["s", "n"]:
            print("Respuesta no válida. Por favor ingrese 'S' o 'N'.")
            tieneCuenta = input("Ya tenés una cuenta? (S/N): ")
    
    
    
        # --- REGISTRO ---
        if tieneCuenta.lower() == "n":
            limpiarConsola()
            
            # 'registrarUsuario' debe devolver True si fue exitoso,
            # o False si el usuario canceló.
            exito_registro = registrarUsuario(USUARIOS) 
            
            if not exito_registro: # Si el usuario canceló (función devolvió False)
                print("Registro cancelado. Volviendo al menú principal.")
                continue # Vuelve al inicio del bucle 'while' (la pregunta S/N)
            
            # Si el registro fue exitoso
            guardarUsuarios(USUARIOS)
            print("Usuario registrado exitosamente. Ahora, por favor iniciá sesión.")
            # El código sigue naturalmente hacia la sección de LOGIN
    
        # --- LOGIN ---
        # Se llega aquí si tieneCuenta == 's' O si el registro fue exitoso
        limpiarConsola()
        print("=== LOGIN ===")
        print("(Escriba 'cancelar' para volver al menú anterior)")
        
        nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
        if nombreUsuario.lower() == "cancelar":
            continue 
        
        contraseña = getpass.getpass("Ingrese su contraseña: ")
        if contraseña.lower() == "cancelar": 
            continue 

        # Buscar el usuario comparando en minusculas (case insensitive)
        nombreUsuarioReal = ""
        for usuario in USUARIOS:
            if usuario.lower() == nombreUsuario.lower():
                nombreUsuarioReal = usuario

        while nombreUsuarioReal == "" or USUARIOS[nombreUsuarioReal]["contrasena"] != contraseña: #muy importante: JSON no entiende la ñ, asi que esta cambiado a contrasena dentro del diccionario
            print("Usuario o contraseña incorrectos. Intente nuevamente, o escriba 'cancelar' para volver al menú anterior.")
            nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
            if nombreUsuario.lower() == "cancelar":
                nombreUsuarioReal = None
                break 
            contraseña = getpass.getpass("Ingrese su contraseña: ")
            if contraseña.lower() == "cancelar":
                nombreUsuarioReal = None
                break
            # Buscar el usuario nuevamente
            nombreUsuarioReal = ""
            for usuario in USUARIOS:
                if usuario.lower() == nombreUsuario.lower():
                    nombreUsuarioReal = usuario

    usuarioLogueado = USUARIOS[nombreUsuarioReal] #obtenemos el diccionario del usuario logueado
    nombreUsuario = nombreUsuarioReal #usamos el nombre real del usuario para las operaciones

    limpiarConsola()
    print(f"Bienvenido, {nombreUsuario}!") #damos la bienvenida al usuario

    opcion = 0
    OPCION_SALIR=7 #por si añadimos mas opciones
    while opcion != OPCION_SALIR:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Reservar un horario")
        print("2. Ver horarios ocupados")
        print("3. Publicar una reserva")
        print("4. Unirse a una reserva publicada")
        print("5. Confirmar pago de reserva")
        print("6. Ver mis reservas")
        print(f"{OPCION_SALIR}. Salir")
        

        try: #este try es para evitar que el programa falle si el usuario ingresa algo que no es un numero
            opcion = int(input(f"Elija una opción (1 - 2 - 3 - 4 - 5 - {OPCION_SALIR}): "))
        except ValueError:
            print("Debe ingresar un número válido.")
            opcion = 0
            continue
        
        if opcion == 1: #reservar un horario
            limpiarConsola()
            reserva = reservar(LISTA_HORARIOS, USUARIOS)
            if reserva != "CANCELAR":
                USUARIOS[nombreUsuario]["reservas"].append(reserva) #agregamos la reserva al usuario logueado
                guardarUsuarios(USUARIOS)
                print("Reserva registrada correctamente!")
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == 2: #ver horarios ocupados
            limpiarConsola()
            deporte = input("Ingrese el deporte para ver las reservas (Futbol, Padel, Tenis) o 'CANCELAR': ")
            if deporte.upper() != "CANCELAR":
                mostrarReservasOcupadas(USUARIOS, deporte) #muestra las reservas ocupadas para el deporte seleccionado
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == 3: #publicar una reserva
            limpiarConsola()
            mostrarMisReservas(usuarioLogueado) #muestra las reservas del usuario logueado
            publicarReserva(usuarioLogueado,nombreUsuario) #publica una reserva privada del usuario logueado
            guardarUsuarios(USUARIOS)
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == 4: #unirse a una reserva publicada
            limpiarConsola()
            unirseReserva(nombreUsuario,USUARIOS) #permite al usuario logueado unirse a una reserva publica
            guardarUsuarios(USUARIOS)
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == 5: #confirmar pago de una reserva
            limpiarConsola()
            mostrarMisReservas(usuarioLogueado) #muestra las reservas del usuario logueado
            confirmarPagoReserva(usuarioLogueado) #marca una reserva como pagada
            guardarUsuarios(USUARIOS)
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == 6: #ver mis reservas
            limpiarConsola()
            mostrarMisReservas(usuarioLogueado) #muestra las reservas del usuario logueado
            input("Presione Enter para continuar...")
            limpiarConsola()
        elif opcion == OPCION_SALIR: #salir del programa
            limpiarConsola()
            guardarUsuarios(USUARIOS) #guarda los datos en el archivo usuarios.json
            print("Adiós!")
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")
            limpiarConsola()

main()