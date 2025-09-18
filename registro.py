import getpass

def registrarUsuario(datos):
        print("")
        print("Registro de usuario")

        usuario = input("Ingrese un nombre de usuario: ")
        while usuario in datos:
            print("El nombre de usuario ya existe. Por favor, elige otro.")
            nombre = input("Ingrese un nombre de usuario: ")

        contraseña = getpass.getpass("Ingrese una contraseña segura: ")

        datos[usuario] = {"contraseña" : contraseña, "reservas": []}

        print("Cuenta creada exitosamente!")