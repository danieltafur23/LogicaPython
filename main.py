# Ejemplo de estacione 
mes = input("Digita un mes del año (TODO MAYUSCULA): ").lower()

if(mes == "enero" or mes == "febrero" or mes == "marzo" or mes == "diciembre"):
    print(f"{mes} se encuentra en Invierno!!")
elif(mes == "junio" or mes == "julio" or mes == "agosto"):
    print(f"{mes} se encuentra en Verano!!")
elif(mes == "abril" or mes == "mayo"):
    print(f"{mes} se encuentra en Primavera!!")
elif(mes == "septiembre" or mes == "octubre" or mes == "noviembre"):
    print(f"{mes} se encuentra en Otoño!!")
else:
    print(f"{mes} no esta bien escrito o no existe este mes del año")
