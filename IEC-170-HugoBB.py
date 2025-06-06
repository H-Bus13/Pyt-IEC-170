from version.version import version
from auxiliares.listas import lnombre, lprecio, lstock, fn_actualizar_lista
from auxiliares.validación_numeros import fn_get_num_valido
from productos.fn_buscar_producto import fn_buscar
from productos.fn_mostrar_producto import fn_mostrar_producto

#Sistema de gestion de inventario para una tienda
#autor: Hugo Bustos

#PROGRAMA PRINCIPAL (PP)
# listas para administrar los productos
try:

    salir = False
    while not salir:
        print(f" *** Menú {version} ***")
        print("[1] Agrega producto")
        print("[2] Listar productos")
        print("[3] Buscar por nombre")
        print("[4] Eliminar producto")
        print("[5] Modificar Producto")
        print("[6] Salir")
        op = input("Opcion: ")
        #****** Agrega producto 
        if (op == "1"):  
            nom = input("Nombre del producto: ")    
            lnombre.append( nom )
            precio = fn_get_num_valido("Precio del producto: ") #float(input("Precio del producto: ") )
            lprecio.append( precio )
            canti = fn_get_num_valido("Cantidad del producto: ") #int(input("Cantidad del producto: ") )
            lstock.append( int(canti))
            fn_actualizar_lista(lnombre, lprecio, lstock)
            print(f"Se ha agregado {nom}, con el precio {precio} y el stock {canti}")
        #****** Listar producto 
        if (op == "2"):  
            largo = len (lnombre)
            for i in range(largo):
                fn_mostrar_producto(lnombre[i], lprecio[i], lstock[i])
        #****** Buscar por Nombre
        if (op == "3"):  
            nom = input("Nombre del producto a buscar: ")    
            pos = fn_buscar(lnombre, nom)
            if pos == -1:
                print(f"El producto {nom} no está en el inventario")
            else:
                fn_mostrar_producto(lnombre[pos], lprecio[pos], lstock[pos])
        #****** Eliminar por Nombre
        if (op == "4"):
            nom = input("Nombre del producto a Eliminar: ")    
            pos = fn_buscar(lnombre, nom)
            if pos != -1: #indica que el producto si está
                fn_mostrar_producto(lnombre[pos], lprecio[pos], lstock[pos])
                resp = input("Seguro que desea eliminar [si/no]: ")
                if resp.upper() == "SI": # nos evitamos el si-Si-sI
                    del lnombre[pos]            # borramos la posicion donde hallamos el producto
                    del lprecio[pos]
                    del lstock[pos]
                    print(f"Producto {nom} eliminado!!.")
                else:
                    print(f"Producto {nom} no se ha eliminado.")
            else:
                print(f"El producto {nom} no está en el inventario")
            #****** Modificar Producto
        if (op == "5"):
            nom = input("Nombre del producto a Modificar: ")   
            pos = fn_buscar(lnombre,nom) 
            if pos == -1: # o sea, no está
                print(f"El producto {nom} no está en el inventario")
            else:    # si efectivamente esta
                fn_mostrar_producto(lnombre[pos], lprecio[pos],lstock[pos])
                resp = input("Seguro que desea modificar [si/no]: ")

                if resp.upper() == "SI": # nos evitamos el si-Si-sI
                    nombre = input("Ingrese un nuevo nombre: ")
                    lnombre[pos] = nombre
                    precio = fn_get_num_valido("Ingrese nuevo precio: ")
                    lprecio[pos] = int(precio) #int(  input("Ingrese nuevo precio: ") )
                    cant = fn_get_num_valido("Ingrese nueva cantidad: ") #int(  input("Ingrese nueva cantidad: ") )
                    lstock[pos] = int(cant)
                    print(f"Stock de {nom} modificado!!.")
                else:
                    print(f"Producto {nom} no se ha modificado.")
        if (op == "6"):
            salir = True
except KeyboardInterrupt as error:
    print("\nUd. ha abandonado el programa por usar la combinacion Ctrl+C")