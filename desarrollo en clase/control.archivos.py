
# archivo = open("archivo.txt", "a", encoding= "utf-8")
# archivo.write("Otro más contenido\n")
# archivo.write("otro más sin sentido\n")
# archivo.close()

# archivo = open ("archivo.txt", "r", encoding= "utf-8")
# contenido = archivo.read()
# print("Contenido del archivo: \n",contenido)

archivo = open ("archivo.txt", "r", encoding= "utf-8")
lineas = archivo.readlines()
numlin = len (lineas)
for i in range (0,numlin):
    lin = lineas[i].strip()
    print(i+1,"\t",lin)