#Sistema de gestion de inventario para una tienda
#autor: Hugo Bustos

#import iec170funciones
from iec170funciones import *
import pickle

"""
version MAJOR.MINOR.PATCH
EJEMPLO v2.4.1

MAJOR: (version mayor): Se incrementa cuando se hacen cambios grandes (generalmente incomptaibles)
    con la version anterior.
MINOR: (version menor): Se incrementa cuando se agregan uevas funcionalidades al sistema, pero 
    sin romper la compatibilidad.
PATCH: (parche o revisión): Se incrementa, cuando se corrigen errores en el sistema, o mejoran 
    funcionalidades 

"""
#Historial 
#       15/04/2025 Inicio del desarrollo v1.0.0
#       22/04/2025 Agrega opción 5 Modificar Cantidad v1.1.0
#       22/04/2025 Mejora las funcionalidades de 3 y 4 al buscar con while v1.1.1
#       29/04/2025 Cambio de paradigma, inicio el trabajo con funciones v2.0.0
#       05/05/2025 Se reemplaza el buscar y mostrar producto por funciones y se 
#                  agregar control de keyboardInterrupt v2.0.1
#       03/06/2025 Se modulariza cada opcion del menu, v2.1.0


def fn_exportar_inventario_csv(lnom, lpre, lsto):
    with open("inventario.csv","w",encoding = "utf-8") as inventario:
        largo = len (lnom)
        for i in range(largo):
            inventario.write(lnom[i]+";"+str( lpre[i]) +";"+str( lsto[i])+"\n")
        print("inventario exportado en inventario.csv")

def fn_guardar_inventario_txt(lnom, lpre, lsto):
    with open("inventario.txt","w",encoding = "utf-8") as inventario:
        largo = len (lnom)
        for i in range(largo):
            inventario.write(lnom[i]+ "\n")
            inventario.write(str( lpre[i]) + "\n" )
            inventario.write(str( lsto[i]) + "\n" )
        print("inventario grabado en inventario.txt")

def fn_cargar_inventario_txt(lnom, lpre, lsto):
    try:
        with open("inventario.txt", "r", encoding="utf-8") as inventario:
            lineas = inventario.readlines()
            largo = len ( lineas ) #cuento el total de líneas
            for  i in range (0, largo, 3 ): #cada producto son 3 líneas
                nom = lineas[i].strip()
                pre = float(lineas[i+1].strip())
                sto = int(lineas[i+2].strip())
                lnom.append( nom )
                lpre.append( pre )
                lsto.append( sto )
        print("Inventario cargado exitosamente.")
    except FileNotFoundError:
        print("No se encontró el inventario, usando por defecto")
        # lnom = ["Plumon", "Borrador", "Pizarra"]
        # lpre = [1280.0, 3500.0, 13500.0]
        # lsto = [20,8, 10]
    except Exception as err:
        print("Error al cargar el inventario:", err)

def fn_guardar_inventario_bin(lnom, lpre, lsto):
    with open("inventario.dat","wb") as inventario:
        pickle.dump((lnom, lpre, lsto), inventario)
        print("inventario grabado en inventario.bin")

def fn_cargar_inventario_bin(lnom, lpre, lsto):
    try:
        with open("inventario.dat","rb") as inventario:
            datos = pickle.load(inventario)
            lnom.extend(datos[0])
            lpre.extend(datos[1])
            lsto.extend(datos[2])
        print("Inventario cargado exitosamente.")    
    
    except FileNotFoundError:
        print("No se encontró el inventario, inventario vacio")
    except Exception as error: 
        print("Oops! algo salio mal, error:", error)

#PROGRAMA PRINCIPAL (PP)
# listas para administrar los productos
lnombre = []
lprecio = []
lstock = []
try:
    version = "v2.1.0"
    # fn_cargar_inventario_txt(lnombre, lprecio, lstock)
    fn_cargar_inventario_bin(lnombre,lprecio,lstock)
    salir = False
    while not salir:
        print(f" *** Menú {version} ***")
        print("[1] Agrega producto")
        print("[2] Listar productos")
        print("[3] Buscar por nombre")
        print("[4] Eliminar producto")
        print("[5] Modificar cantidad")
        print("[6] Exportar inventario")
        print("[7] Salir")
        op = input("Opcion: ")
        #****** Agrega producto 
        if (op == "1"):  
            fn_agregar_producto(lnombre, lprecio, lstock)

        #****** Listar producto 
        if (op == "2"):  
            fn_listar_producto(lnombre, lprecio, lstock)

        #****** Buscar por Nombre   
        if (op == "3"):  
            fn_buscar_producto(lnombre, lprecio, lstock)

        #****** Eliminar por Nombre
        if (op == "4"):
            fn_eliminar_producto(lnombre, lprecio, lstock)

        #****** Modificar Cantidad
        if (op == "5"):
            fn_modificar_producto(lnombre, lprecio, lstock)
        
        if (op == "6"):
            fn_exportar_inventario_csv(lnombre,lprecio,lstock)

        if (op == "7"):
            salir = True
            # fn_guardar_inventario_txt(lnombre, lprecio, lstock)
            fn_guardar_inventario_bin(lnombre,lprecio,lstock)
            print("Hasta luego")

except KeyboardInterrupt as error:
    print("\nUd. ha abandonado el programa por usar la combinacion Ctrl+C")