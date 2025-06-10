import bcrypt
import pwinput

palabra = pwinput.pwinput(prompt="clave: ",mask= "?")

contrasena = palabra.encode("utf-8")
print("contraseña:",contrasena)
hash_contrasena = bcrypt.hashpw(contrasena, bcrypt.gensalt())

print(hash_contrasena)


# pwinput.pwinput(prompt="clave: ",mask= "?")