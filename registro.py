"""
Módulo de registro de usuarios
"""
import getpass

def registrarUsuario(dictUsuarios):
        """
        Registra un nuevo usuario en el sistema.
        Valida nombre de usuario (mínimo 3 caracteres) y contraseña (mínimo 4 caracteres).
        """
        print("")
        print("Registro de usuario. (Escriba 'cancelar' en cualquier momento para volver al menú anterior)")

        usuario = input("Ingrese un nombre de usuario (mínimo 3 caracteres): ").strip()
        if usuario.lower() == "cancelar":
            return False  # Usuario canceló el registro

        # Crear lista de usuarios en minusculas para verificar case insensitive
        usuariosLower = [usuarioExistente.lower() for usuarioExistente in dictUsuarios.keys()]

        while len(usuario) < 3 or usuario.lower() in usuariosLower:
            if len(usuario) < 3:
                print("El nombre de usuario debe tener al menos 3 caracteres.")
            elif usuario.lower() in usuariosLower:
                print("El nombre de usuario ya existe. Por favor, elige otro.")
            usuario = input("Ingrese un nombre de usuario (mínimo 3 caracteres): ").strip()
            if usuario.lower() == "cancelar":
                return False  # Usuario canceló el registro
            # Actualizar lista de usuarios en minusculas
            usuariosLower = [usuarioExistente.lower() for usuarioExistente in dictUsuarios.keys()]

        # Validar longitud mínima de contraseña (4 caracteres)
        contraseña = getpass.getpass("Ingrese una contraseña segura (mínimo 4 caracteres): ")
        if contraseña.lower() == "cancelar":
            return False  # Usuario canceló el registro

        while len(contraseña) < 4:
            print("La contraseña debe tener al menos 4 caracteres.")
            contraseña = getpass.getpass("Ingrese una contraseña segura (mínimo 4 caracteres): ")
            if contraseña.lower() == "cancelar":
                return False  # Usuario canceló el registro

        dictUsuarios[usuario] = {"contrasena" : contraseña, "reservas": []}

        print("Cuenta creada exitosamente!")
        return True  # Registro exitoso