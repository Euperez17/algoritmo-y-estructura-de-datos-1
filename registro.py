import getpass

def registrarUsuario(datos):
        print("")
        print("Registro de usuario")

        usuario = input("Ingrese un nombre de usuario: ")
        while usuario in [u[0] for u in datos]:
            print("El nombre de usuario ya existe. Por favor, elige otro.")
            usuario = input("Ingrese un nombre de usuario: ")

        contraseña = getpass.getpass("Ingrese una contraseña segura: ")
        datos.append([usuario, contraseña, []])
        print("Cuenta creada exitosamente!")