#ejercicio #1

#age = int(input("Por favor, ingrese su edad: "))
#
#if age > 18:
#    print("Es mayor de edad.")
#else:
#    pass    
#

#ejercicio #2
#calification = int(input("Por favor, ingrese su calificacion: "))
#
#if calification >= 6:
#    print("Aprobado")
#elif calification < 6:
#    print("Desaprobado")

#ejercicio #3
#even_number = int(input("Por favor, ingrese un numero: "))
#
#if even_number % 2 == 0:
#    print("Ha ingresado un numero par.")
#else:
#    print("Por favor, ingrese un numero par.")

#ejercicio #4

#age = int(input("Por favor ingrese su edad: "))
#
#if age < 18:
#    if age >= 12:
#        print("Usted es un adolescente")
#    else:
#        print("Usted es un ninio.")
#else:
#    if age >= 18 and age < 30:
#        print("Usted es un adulto joven.")
#    else:
#        print("Usted es un adulto.")

#ejercicio #5


#password = input("Por favor, ingrese una contrasena que contenga entre 8 y 14 caracteres: ")
#lenght = len(password)

#primera forma de acercamiento
#if len(password) < 14 and len(password)> 8:
#    print("Ha ingresado una contrasena correcta.")
#else:
#    print("Por favor, ingrese una contrasena de entre 8 y 14 caracteres")

#segunda forma de acercamiento
#if password.__len__() < 14 and password.__len__() > 8:
#    print("Ha ingresado una contrasena correcta.")
#else:
#    print("Por favor, ingrese una contrasena de entre 8 y 14 caracteres")

#tercera forma de acercamiento
#if 8 < len(password) < 14:
#    print("Ha ingresado una contrasena correcta.")
#else:
#    print("Por favor, ingrese una contrasena de entre 8 y 14 caracteres")

#ejercicio #6
#import random
#from statistics import mode, median, mean

#numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

#_mode = mode(numeros_aleatorios)
#_median = median(numeros_aleatorios)
#_mean = mean(numeros_aleatorios)

#text = input("que desea calcular? mode, median or mean?: ")
#if text == "mode":
#    print(f"La moda de los numeros aleatorios es: {_mode}")
#elif text == "median":
#    print(f"La mediana de los numeros aleatorios es: {_median}")
#elif text == "mean":
#    print(f"La media de los numeros aleatorios es: {_mean}")
#else:
#    print("Opcion, invalida. Reintente otra vez.")

#ejercicio #7
#text = input("Ingrese una frase o palabra: ").strip()

#if len(text) > 0:
#    last_character = text.rstrip()[-1].lower()

#    if last_character in 'aeiou':
#        print(text + '!')
#    else:
#        print(text)
#else:
#    print("Debes ingresar algo, el campo no puede estar vacio.")

#ejercicio 8:

#name = input("Ingrese su nombre: ")
#number = int(input("Ingrese 1, 2 o 3: "))

#if number == 1:
#    print(name.upper())
#elif number == 2:
#    print(name.lower())
#elif number == 3:
#    print(name.title())        
#else:
#    print("Solo son validos los numeros 1, 2 y 3")

#ejercicio #9

scale = int(input("Ingrese la magnitud del terremeto en escala de Ritcher: "))

if scale < 3:
    print("Muy leve")
else: 
    if scale >= 3 and scale < 4:
        print("Leve")
    if scale >= 4 and scale < 5:
        print("Moderado")
    if scale >= 5 and scale < 6:
        print("Fuerte")
    if scale >= 6 and scale < 7:
        print("Muy fuerte")
    if scale >= 7:
        print("Extremo")
# 
# Actividad realizada por Cerdan, Marcos        