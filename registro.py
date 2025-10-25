import getpass

def registrarUsuario(datos):
        print("")
        print("Registro de usuario")

        # Validar longitud mínima de usuario (3 caracteres)
        usuario = input("Ingrese un nombre de usuario (mínimo 3 caracteres): ").strip()
        while len(usuario) < 3 or usuario in datos:
            if len(usuario) < 3:
                print("El nombre de usuario debe tener al menos 3 caracteres.")
            elif usuario in datos:
                print("El nombre de usuario ya existe. Por favor, elige otro.")
            usuario = input("Ingrese un nombre de usuario (mínimo 3 caracteres): ").strip()

        # Validar longitud mínima de contraseña (4 caracteres)
        contraseña = getpass.getpass("Ingrese una contraseña segura (mínimo 4 caracteres): ")
        while len(contraseña) < 4:
            print("La contraseña debe tener al menos 4 caracteres.")
            contraseña = getpass.getpass("Ingrese una contraseña segura (mínimo 4 caracteres): ")

        datos[usuario] = {"contrasena" : contraseña, "reservas": []}

        print("Cuenta creada exitosamente!")