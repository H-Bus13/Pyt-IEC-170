# import getpass
import pwinput 

usuario = input("usuario: ")
clave = pwinput.pwinput(prompt="clave: ",mask= "?")

if usuario == "admin" and clave == "123456":
    print("Acceso concedido.")
else:
    print("Acceso denegado.")


print(f"Las credenciales son {usuario} y {clave}")

