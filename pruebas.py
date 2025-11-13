import os
import json
import copy
from reservas import buscarHorariosReservados, horarioEstaOcupado

DATA_USUARIOS_PATH = os.path.join(os.path.dirname(__file__), "data", "usuarios.json") #Ruta al archivo usuarios.jason

with open(DATA_USUARIOS_PATH, "r", encoding="utf-8") as archivo:
    USUARIOS = json.load(archivo)

def test_usuarios_existe(): #Verifica que usuarios.json existe y contiene al menos un usuario.
    assert os.path.exists(DATA_USUARIOS_PATH), f"No se encontró {DATA_USUARIOS_PATH}"
    assert len(USUARIOS) > 0, "El archivo usuarios.json está vacío" #usuarios.json tiene que tener al menos un usuario

def test_usuario_estructura_correcta(): #Verifica que cada usuario tiene 'contrasena' y 'reservas'.
    # Obtener el primer usuario del diccionario
    nombres_usuarios = list(USUARIOS.keys())
    nombre = nombres_usuarios[0]
    datos = USUARIOS[nombre]

    assert "contrasena" in datos, f"El usuario {nombre} debe tener la clave 'contrasena'"
    assert "reservas" in datos, f"El usuario {nombre} debe tener la clave 'reservas'"

def test_buscar_horarios_reservados():#Prueba la función buscarHorariosReservados.
    resultado = buscarHorariosReservados(USUARIOS)
    assert type(resultado) == list, "buscarHorariosReservados debe devolver una lista" #debe devolver una lista

def test_horario_esta_ocupado(): #Prueba la función horarioEstaOcupado.
    reservados = [ #Creo una lista de reservas de prueba
        {"Deporte": "Tenis", "Horario": "14:00"},
        {"Deporte": "Futbol", "Horario": "15:00"}
    ]
    assert horarioEstaOcupado(reservados, "Tenis", "14:00") == True, "Debe detectar horario ocupado" #tenis 14:00 está ocupado
    assert horarioEstaOcupado(reservados, "Tenis", "16:00") == False, "Debe detectar horario libre" #tenis 16:00 debería estar libre
    assert horarioEstaOcupado(reservados, "Padel", "14:00") == False, "Debe detectar horario libre para otro deporte" #padel 14:00 debería estar libre

def test_publicar_reserva(): #Simula publicar una reserva sin usar input().
    # Obtener el primer usuario del diccionario
    nombres_usuarios = list(USUARIOS.keys())
    nombre = nombres_usuarios[0]
    datos_original = USUARIOS[nombre]
    usuario = copy.deepcopy(datos_original) #clonamos el usuario para no modificar el original
    print("Usuario de prueba:", nombre)

    # Crear una reserva privada de prueba si no existe
    if "reservas" not in usuario or type(usuario["reservas"]) != list:
        usuario["reservas"] = []
    if len(usuario["reservas"]) == 0:
        usuario["reservas"].append({
            "Deporte": "Futbol",
            "Horario": "14:00",
            "Integrantes": "privado"
        })

    # Simular publicar la primera reserva privada
    reservas_privadas = [reserva for reserva in usuario["reservas"] if reserva.get("Integrantes") == "privado"]
    if reservas_privadas:
        reserva = reservas_privadas[0]
        reserva["Integrantes"] = [nombre]
        reserva["CupoMaximo"] = 4  # valor de ejemplo

    # Verificar que la reserva tiene la estructura correcta después de publicar
    reserva_publicada = usuario["reservas"][0]
    assert nombre in reserva_publicada["Integrantes"], "El usuario debe estar en 'Integrantes'"
    assert reserva_publicada["Deporte"] == "Futbol", "El deporte debe ser 'Futbol'"
    assert reserva_publicada["Horario"] == "20:00", "La reserva debe ser a las 20:00"
    