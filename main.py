""" 
Una agencia de viajes necesita un programa para gestionar la oferta de paquetes turísti-cos que ofrece.
Para ello cuenta con un archivo de texto con formato CSV donde cada registro contiene los siguientes campos:
∑Ciudad de destino
∑Región (Opciones posibles: Argentina, Brasil, Caribe, EEUU, Europa, Oriente, Otros)
∑Fecha de salida (DDMMAAAA)
∑Cantidad de noches de hotel
∑Medio de transporte (*)
∑Precio por pasajero
∑Régimen de comidas 
(**)(*) Tabla de abreviaturas del medio de transporte
ST Sin transporte; el mismo va por cuenta del cliente
SC Bus semi cama
BC Bus cama
AE Aéreo
(**) Tabla de abreviaturas del régimen de comidas
CP Continental Plan (Con desayuno)
BB Buffet Breakfast (Desayuno buffet)
MAP Modified American Plan(Media pensión)
FAP Full American Plan(Pensión completa)
AI All Inclusive Plan(Todo incluido)

El Trabajo Práctico consiste en desarrollar un programa que permita realizar búsquedas por cualquiera de los campos presentes
en cada registro, y que muestre por pantalla todos los paquetes turísticos existentes para ese criterio, ordenando el listado
en forma ascendente según la fecha de salida. Si existieran varios paquetes con la misma fecha de salida el ordenamiento
secundario será según el precio por persona, también en forma ascendente. No hay un máximo preestablecido para la cantidad de
registros del archivo.
Se suministra un archivo ejemplo llamado "paquetes.txt" con 190 registros. Se recomienda que la entrega
contenga no menos de 500 registros.
""" 



"""
1 - Crear funcion para mostrar menu con opciones de entrada/salida , compra 
2 - crear función compra que liste todos los paquetes segun fechas de viaje. Si existieran varios paquetes con la misma fecha de salida el ordenamiento
secundario será según el precio por persona(tener en cuenta estetica).
3 - crear funcion de filtros debe permitir filtrar por medio de transporte, precio menor a mayor 
    y viceversa, y regimenes de comida. (Tener en cuenta que debe mantener filtros ya hechos y poder deshacer anteriores)
4- crear funcion que permita realizar la compra y que pida datos ficticios de la tarjeta debito/credito y solicite mail para mandar correo (crear archivo final con detalle de compra)


################## MENU ######################
Bienvenido a Aventura Turismo, elija la opción que desea realizar:
    1 -  Comprar paquetes turisticos
    2 -  Salir
################## COMPRAR ######################
1-  ∑Región : Argentina                     Fecha de salida (DDMMAAAA)
    ∑Ciudad de destino : Cordoba            Cantidad de noches de hotel
    ∑Medio de transporte (*)                ∑Régimen de comidas
    ∑Precio por pasajero
2-  ∑Región : Argentina                     Fecha de salida (DDMMAAAA)
    ∑Ciudad de destino : Cordoba            Cantidad de noches de hotel
    ∑Medio de transporte (*)                ∑Régimen de comidas
    ∑Precio por pasajero
3-  ∑Región : Argentina                     Fecha de salida (DDMMAAAA)
    ∑Ciudad de destino : Cordoba            Cantidad de noches de hotel
    ∑Medio de transporte (*)                ∑Régimen de comidas
    ∑Precio por pasajero
################## FILTROS ######################
Desea filtrar por:
    1 - Precio
    2 - Medio de transporte
    3 - Comida
    4 - No requiero filtrar, quiero realizar la compra
    5 - No quiero comprar, salir
################## REALIZAR COMPRA ######################
Cuales de los paquetes desea comprar?(Indique número):
################## PAGO ######################
Para finalizar la compra se le solicita lo siguiente(En caso de arrepentimiento apretar -1):
NOMBRE Y APELLIDO:

NRO. DE TARJETA: 

FECHA DE VENCIMIENTO:

CODIGO:

CORREO ELECTRONICO:
################## FINALIZAR ######################
Le estara llegando a su correo electronico el detalle de la compra.
Agradecemos su visita. Tenga un buen viaje.


################## DETALLE DE PAGO ######################
Nombre y Apellido

∑Región : Argentina                     Fecha de salida (DDMMAAAA)
∑Ciudad de destino : Cordoba            Cantidad de noches de hotel
∑Medio de transporte (*)                ∑Régimen de comidas
∑Precio por pasajero

Pagado con Nro de tarjeta



"""
def listarPaquetesTuristicos(paquetes,titulos):
    cant = 0
    listaDePaquetes = []

    for valor in paquetes:
        diccionario = {}
        for i in range(len(titulos)):
            diccionario[titulos[i]] = valor[i]
        listaDePaquetes.append(diccionario)
    print(listaDePaquetes)

    print("################## COMPRAR ######################")
    for paquete in listaDePaquetes:
        cant += 1
        print(f"{cant}-")
        print(f"    Ciudad de destino: {paquete['Ciudad de destino']}               Región: {paquete['Región']}\n")
        print(f"    Fecha de salida: {paquete['Fecha de salida']}               Cantidad de noches de hotel: {paquete['Cantidad de noches de hotel']}\n")
        print(f"    Medio de transporte: {paquete['Medio de transporte']}               Régimen de comidas: {paquete['Régimen de comidas']}\n")
        print(f"    Precio por pasajero: {paquete['Precio por pasajero']}\n")
            


def mostrarMenu(paquetes, titulos):
    print("=== MENU ===")
    print("1. Comprar paquetes turisticos")
    print("4. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        listarPaquetesTuristicos(paquetes,titulos)
    elif opcion == 4:
        print("Hasta luego!")
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")




#MAIN
datos=[]
claves = ['Ciudad de destino', 'Región', 'Fecha de salida', 'Cantidad de noches de hotel', 'Medio de transporte', 'Precio por pasajero', 'Régimen de comidas']
try:
    arch = open("Paquetes copy.txt","r")
    linea = arch.readline()
    while linea:
        valores = linea.split(';')
        print(valores)
        datos.append(valores)
        linea = arch.readline()
    mostrarMenu(datos, claves)
except OSError as mensaje:
    print("Hubo un inconveniente al leer el archivo:", mensaje)
finally:
    arch.close()
