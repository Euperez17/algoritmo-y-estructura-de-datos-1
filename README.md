# 🏟️ Sistema de Reservas de Canchas Deportivas

Sistema integral de gestión de reservas para un complejo deportivo, desarrollado en Python. Permite a los usuarios registrarse, reservar horarios para diferentes deportes, publicar reservas para jugar en grupo y gestionar pagos.

## 📋 Descripción

Este proyecto implementa un sistema completo de reservas de canchas deportivas que permite:
- Registro y autenticación de usuarios
- Reserva de horarios para Fútbol, Pádel y Tenis
- Sistema de reservas privadas y públicas
- Gestión de grupos y cupos máximos por deporte
- Seguimiento de estado de pagos
- Persistencia de datos mediante archivos JSON

## 🚀 Características Principales

### Gestión de Usuarios
- **Registro seguro**: Validación de nombres de usuario (mínimo 3 caracteres) y contraseñas (mínimo 4 caracteres)
- **Login con seguridad**: Uso de `getpass` para ocultar contraseñas
- **Validación case-insensitive**: Los nombres de usuario no distinguen entre mayúsculas y minúsculas

### Sistema de Reservas
- **Reservas privadas**: Reserva personal de horarios
- **Reservas públicas**: Publicación de reservas para que otros usuarios se unan
- **Control de cupos**: Límite de jugadores por deporte (Fútbol: 22, Pádel: 4, Tenis: 4)
- **Validación de horarios**: Solo muestra horarios disponibles según la hora actual
- **Gestión de pagos**: Marcar reservas como pagadas

### Deportes Disponibles
- **⚽ Fútbol** - Capacidad: 22 jugadores
- **🎾 Pádel** - Capacidad: 4 jugadores
- **🎾 Tenis** - Capacidad: 4 jugadores

### Horarios Disponibles
```
08:00 | 09:30 | 11:00 | 12:30 | 14:00 | 15:30 | 17:00 | 18:30 | 20:00 | 21:30 | 23:00
```

## 🛠️ Requisitos Técnicos

### Dependencias
- **Python 3.7+**
- **pytest** (para ejecutar las pruebas)

### Instalación
```bash
# Clonar el repositorio
git clone https://github.com/Euperez17/algoritmo-y-estructura-de-datos-1.git

# Navegar al directorio
cd algoritmo-y-estructura-de-datos-1

# Instalar pytest (opcional, para pruebas)
pip install pytest
```

## 📂 Estructura del Proyecto

```
algoritmo-y-estructura-de-datos-1/
│
├── app.py                      # Programa principal con menú y flujo de la aplicación
├── reservas.py                 # Módulo de gestión de reservas
├── registro.py                 # Módulo de registro de usuarios
├── utilidades.py               # Funciones auxiliares (cargar/guardar datos, limpiar consola)
├── constantes.py               # Constantes del sistema (deprecado)
├── pruebas.py                  # Suite de pruebas unitarias
│
├── data/
│   ├── usuarios.json           # Base de datos de usuarios
│   ├── horarios.json           # Horarios disponibles por deporte
│   └── capacidad_maxima.json   # Capacidad máxima por deporte
│
├── .gitignore
└── README.md
```

## 🎮 Uso del Sistema

### Ejecución
```bash
python app.py
```

### Flujo de Uso

#### 1. Inicio de Sesión
```
- ¿Ya tenés una cuenta? (S/N)
  - Si NO: Registrarse con usuario y contraseña
  - Si SÍ: Ingresar credenciales
```

#### 2. Menú Principal
```
--- MENÚ PRINCIPAL ---
1. Reservar un horario
2. Ver horarios ocupados
3. Publicar una reserva
4. Unirse a una reserva publicada
5. Confirmar pago de reserva
6. Ver mis reservas
7. Salir
```

#### 3. Funcionalidades Detalladas

**Reservar un horario (Opción 1)**
- Seleccionar deporte (Futbol, Padel, Tenis)
- Ver horarios disponibles según la hora actual
- Elegir horario deseado
- La reserva se crea como privada por defecto

**Ver horarios ocupados (Opción 2)**
- Seleccionar deporte
- Ver todos los horarios ya reservados por otros usuarios

**Publicar una reserva (Opción 3)**
- Seleccionar una de tus reservas privadas
- Convertirla en pública para que otros se unan
- Se establece el cupo máximo según el deporte

**Unirse a una reserva publicada (Opción 4)**
- Ver todas las reservas públicas disponibles
- Seleccionar una reserva
- Unirse si hay cupo disponible

**Confirmar pago de reserva (Opción 5)**
- Ver tus reservas pendientes de pago
- Marcar como pagada la reserva seleccionada

**Ver mis reservas (Opción 6)**
- Visualizar todas tus reservas activas
- Ver deporte, horario, integrantes y estado de pago

## 🧪 Pruebas Unitarias

El proyecto incluye una suite de pruebas automatizadas en [pruebas.py](pruebas.py).

### Ejecutar Pruebas
```bash
# Con pytest
python -m pytest pruebas.py -v

# O directamente con Python
python pruebas.py
```

### Pruebas Incluidas
- ✅ `test_usuarios_existe()` - Verifica la existencia del archivo de usuarios
- ✅ `test_usuario_estructura_correcta()` - Valida la estructura de datos de usuarios
- ✅ `test_buscar_horarios_reservados()` - Prueba la búsqueda de reservas
- ✅ `test_horario_esta_ocupado()` - Verifica detección de horarios ocupados
- ✅ `test_publicar_reserva()` - Simula la publicación de una reserva

**Resultado esperado:** 5/5 PASSED ✅

## 📊 Persistencia de Datos

### Archivos JSON

**usuarios.json**
```json
{
    "nombreUsuario": {
        "contrasena": "password123",
        "reservas": [
            {
                "Deporte": "Futbol",
                "Horario": "20:00",
                "Integrantes": ["usuario1", "usuario2"],
                "CupoMaximo": 22,
                "Pagado": false
            }
        ]
    }
}
```

**horarios.json**
```json
{
    "Futbol": ["08:00", "09:30", "11:00", ...],
    "Padel": ["08:00", "09:30", "11:00", ...],
    "Tenis": ["08:00", "09:30", "11:00", ...]
}
```

**capacidad_maxima.json**
```json
{
    "Futbol": 22,
    "Padel": 4,
    "Tenis": 4
}
```

## 🔧 Funcionalidades Técnicas Destacadas

### Validaciones Implementadas
- ✅ Validación de longitud mínima de usuario y contraseña
- ✅ Verificación de usuarios duplicados (case-insensitive)
- ✅ Validación de horarios disponibles según la hora actual
- ✅ Control de cupos máximos por deporte
- ✅ Manejo de errores con try-except
- ✅ Opción de cancelar en cualquier momento

### Características de UX
- ✅ Limpieza de consola multiplataforma (Windows/Linux/Mac)
- ✅ Mensajes informativos claros
- ✅ Contraseñas ocultas con getpass
- ✅ Navegación intuitiva con opciones de cancelar

## 📝 Historial de Versiones

Ver [ERRORES_Y_SOLUCIONES.md](ERRORES_Y_SOLUCIONES.md) para el registro detallado de errores encontrados y soluciones aplicadas durante el desarrollo.
