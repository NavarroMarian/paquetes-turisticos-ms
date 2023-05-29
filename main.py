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
