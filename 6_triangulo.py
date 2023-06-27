'''6. Escribe un script que solicite la base y 
la altura de un triángulo, calcule su área e imprima el resultado'''

print('Vamos a calcular el área de un triángulo')
print('')
b = float(input('Dame el valor de la base en cm: ' ))
h = float(input('Dame la altura en cm: ' ))

area = (b*h)/2

print(f'El área del triángulo con altura de {h} cm  y base de {b} cm es de {round(area,1)} cm.')