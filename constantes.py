# Hasta que aprendamos a usar archivos, hardcodeamos este diccionario para el login
USUARIOS = {
    "dante": {"contraseña": "1234",
              "reservas": [{ #reservas es una lista de diccionarios e integrantes contiene nombres de usuario de los integrantes
                        "Deporte": "Futbol",
                        "Horario":"20:00",
                        "Integrantes": ["dante"],
                        "CupoMaximo": 22
                    },
                    {
                        "Deporte":"Padel",
                        "Horario":"08:00",
                        "Integrantes":"privado"
                    }
                    ]
            },
    "augus": {"contraseña": "5678", "reservas": []}
} #estructura: nombre, contraseña, reservas hechas
#estructura reservas hechas: deporte, horario, integrantes, -1 si es privada

# Constante de diccionario con los horarios posibles por deporte
LISTA_HORARIOS = {
    "Futbol": ["08:00", "09:30", "11:00", "12:30", "14:00", "15:30", "17:00", "18:30", "20:00", "20:30", "22:00"],
    "Padel": ["08:00", "09:30", "11:00", "12:30", "14:00", "15:30", "17:00", "18:30", "20:00", "20:30", "22:00"],
    "Tenis": ["08:00", "09:30", "11:00", "12:30", "14:00", "15:30", "17:00", "18:30", "20:00", "20:30", "22:00"]
}

# Capacidad maxima de jugadores por deporte
CAPACIDAD_MAXIMA = {
    "Futbol": 22,
    "Padel": 4,
    "Tenis": 4
}