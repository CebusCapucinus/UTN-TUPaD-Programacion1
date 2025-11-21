#ejercitacion unidad 4
#ejercicio #1
#def printer():
#    for i in range(0,101):
#        print(i)
#
#print(printer())


#ejercicio #2
#def printed_number():
#   input_number = int(input("Ingrese un numero: "))
#
#    print(input_number, "posee {} digito/s".format(len(str(input_number))))
#    return
#print(printed_number())

#ejercicio #3

#first_number = int(input("Ingrese un numero: "))
#second_number = int(input("Ingrese otro numero: "))
#suma = 0
#for i in range(first_number, second_number):
#    suma += i

#print("La suma de los numeros entre", first_number, "y", second_number, "es:", suma)

#ejercicio #4

total = 0
number = 1

print("Ingrese los numeros que desea sumar. Ingrese 0 para finalizar.")

while number != 0:
    number = int(input("Numero: "))
    total += number

total -= 0
print("Total acumulado:", total)    