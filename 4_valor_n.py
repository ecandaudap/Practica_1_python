'''4. Escribe un script que solicite un número (n) y 
calcule el valor de n + nn + nnn'''

n = int(input('Dame un número entero: '))

suma = n + pow(n,2) + pow(n,3)

print(f'El resultado de sumar el número {n} a su cuadrado y a su cubo es: {int(suma)}')