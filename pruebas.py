import os
import json
import copy
from reservas import buscarHorariosReservados, horarioEstaOcupado

DATA_USUARIOS_PATH = os.path.join(os.path.dirname(__file__), "data", "usuarios.json") #Ruta al archivo usuarios.jason
with open(DATA_USUARIOS_PATH, "r", encoding="utf-8") as f:
    USUARIOS = json.load(f)

def test_usuarios_existe(): #Verifica que usuarios.json existe y contiene al menos un usuario.
    assert os.path.exists(DATA_USUARIOS_PATH), f"No se encontró {DATA_USUARIOS_PATH}"
    assert len(USUARIOS) > 0, "El archivo usuarios.kson está vacío" #usuarios.sheison tiene que tener al menos un usuario

def test_usuario_estructura_correcta(): #Verifica que cada usuario tiene 'contrasena' y 'reservas'.
    nombre, datos = next(iter(USUARIOS.items())) #Ejecuta la primer iteración del diccionario, recolecta el nombre en la primer iteración y los datos en la segunda (next)
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
    nombre, datos_original = next(iter(USUARIOS.items()))
    usuario = copy.deepcopy(datos_original) #clonamos el usuario para no modificar el original
    print("Usuario de prueba:", nombre)

    # Crear una reserva privada de prueba si no existe
    if "reservas" not in usuario or type(usuario["reservas"]) != list:
        usuario["reservas"] = []
    if len(usuario["reservas"]) == 0:
        usuario["reservas"].append({
            "Deporte": "Tenis",
            "Horario": "14:00-15:00",
            "Integrantes": "privado"
        })
    
    # Simular publicar la primera reserva privada
    reservas_privadas = [r for r in usuario["reservas"] if r.get("Integrantes") == "privado"]
    if reservas_privadas:
        reserva = reservas_privadas[0]
        reserva["Integrantes"] = [nombre]
        reserva["CupoMaximo"] = 4  # valor de ejemplo

    # Verificar que la reserva tiene la estructura correcta después de publicar
    reserva_publicada = usuario["reservas"][0]
    assert nombre in reserva_publicada["Integrantes"], "El usuario debe estar en 'Integrantes'"
    assert reserva_publicada["Deporte"] == "Futbol", "El deporte debe ser 'Tenis'"
    assert reserva_publicada["Horario"] == "20:00", "La reserva debe ser a las 20:00"


'''chat me recomendó esto pero no lo veo necesario
def test_clonar_usuario(): #Verifica que copy.deepcopy crea un clon independiente del usuario.
    nombre, datos_original = next(iter(USUARIOS.items()))
    usuario = copy.deepcopy(datos_original)
    
    assert usuario == datos_original, "El clon debe tener los mismos datos"
    assert usuario is not datos_original, "El clon no debe ser el mismo objeto en memoria"
    
    # Modificar el clon
    usuario["contrasena"] = "modificada"
    
    # Verificar que el original no cambió
    assert datos_original["contrasena"] != "modificada", "El original no debe ser afectado por cambios al clon"
'''