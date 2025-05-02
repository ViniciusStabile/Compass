"""
Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:

Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
"""

import random

random_list = random.sample(range(500), 50)

random_list.sort()

mediana = (random_list[24] + random_list[25]) / 2
media = sum(random_list) / 50
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f"Media: {media:.2f}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")
