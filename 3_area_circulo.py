'''3. Escribe un script que calcule el área de un círculo 
basado en el radio proporcionado por el usuario e imprima el resultado.
'''

import numpy as np

print('Vamos a calcular el área de un circulo')
print('')
radio = input('Dame el valor del radio en cm: ' )

area = np.pi*float(radio)

print(f'El área del circulo con radio de {radio} cm es de {round(area,1)} cm.')