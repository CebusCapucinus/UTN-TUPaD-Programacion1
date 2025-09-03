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