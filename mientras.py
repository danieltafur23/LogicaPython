#importat librerias(Codigos prefabricados)
import math

#declaro el ciclo
print("Empanadas el machetico")
print("*****")
print("0. Para salir")
print("1. Para calcular la raiz cuadrada de un #")
print("2. Para calcular la potencia 2 de un #")
print("*****")
opcion = 1

while(opcion != 0 ):

    opcion = int(input("Digite una opcion: "))

    #pregunte por la opcion
    if(opcion == 1):
        numero1 = int(input("Digita un numero: "))
        raiz = math.isqrt(numero1)
        print(f"La raiz de {numero1} es: {raiz}")

    elif(opcion == 2):
        numero2 = int(input("Digite un numero: "))
        resultado = math.pow(numero2, 2)
        print(f"El {numero2} elevado al cuadrado es: {resultado}")

    else:
        print("Digite una opcion valida")
