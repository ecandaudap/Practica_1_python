'''2. Escribe un programa que solicite el nombre, el apellido y la edad del usuario 
e imprima un saludo y su año de nacimiento. Tomar el año actual como constante (2023)

Ejemplo.
input
Nombre: Alfredo
Apellido: Altamirano
Edad: 36

output
Hola Alfredo Altamirano, naciste en 1986
'''

nombre = input("Dame tu nombre: ")
apellido = input("Escribe tu apellido paterno: ")
edad = input("Escribe tu edad: ")
year = 2023 - int(edad)

print(f'Hola {nombre} {apellido}, naciste en {year}')