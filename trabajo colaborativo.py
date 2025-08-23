# ejercicio #1
# print ("Hello world")

# ejercicio #2
# name = input("Ingrese su nombre: ")
# print(f"Hola {name}")

# ejercicio #3
#name = input("Ingrese su nombre: ")
#surname = input ("Ingrese su apellido: ")
#age = input ("Ingrese su edad: ")
#localization = input ("Ingrese su localidad de residencia: ")
#print(f"Soy {surname}, {name}. Tengo {age} años y vivo en {localization}")

# ejercicio #4
#pi = 3.14
#radio = int(input ("Enter the radious of the circle that you desire to calculate: "))
#Area = pi * (radio * radio)
#Perimeter = 2 * pi * radio
#print(f"The area of your circle is: {Area}")
#print(f"The perimeter of your circle is: {Perimeter}")

# ejercicio #5
#seconds = int(input("Enter the seconds that you want to convert to hours: "))
#hours = seconds / 3600
#print(f"The equivalent is: {hours} hours")

# ejercicio #6
#def multiplication_table (number):
#
#    for factor in range (1, 11):
#        result = number * factor
#        print(f"{number} x {factor} = {result}")

#user_number = int(input("Enter a number to show the multiplication table: "))
#multiplication_table(user_number)

# ejercicio #7

#def number_table (x, y):
#        sum = x + y 
#        print(f"your sum is: {sum}")
#
#user_number_x = int(input("Enter a number between 0 and 10: "))
#user_number_y = int(input("Enter another number between 0 and 10: "))
#number_table(user_number_x, user_number_y)

# ejercicio #8
#def imc(mass, height):
#        return mass / (height ** 2 )

#mass = float(input("Enter your mass expressed in kilograms: "))
#height = float(input("Enter your height expressed in meters: "))
#imc_value = imc(mass, height)

#print(f"Your IMC is: {imc_value:.1f}")

#ejercicio 9
#def conversion_formula (celsius):
#    return (9/5) * celsius + 32

#celsius = float(input("Enter the temperature in celsius: "))
#conversion = conversion_formula(celsius)

#print(f"Your temperature in farenheit is: {conversion} ")

#ejercicio 10
def average (number_one, number_two, number_tree):
    
    return (number_one + number_two + number_tree) / 3

number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the sencond number: "))
number_tree = int(input("Enter the third number: "))

result = average(number_one, number_two, number_tree)

print(f"The average is: {result}")

#Trabajo realizado por Cerdan, Marcos Samuel