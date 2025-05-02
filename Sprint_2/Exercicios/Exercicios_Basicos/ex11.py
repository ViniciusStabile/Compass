"""
Escreva uma função que recebe como parâmetro uma lista e 
retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""


def func(entrada):
    terco = len(entrada) // 3
    terco2 = terco * 2
    lista1 = entrada[:terco]
    lista2 = entrada[terco:terco2]
    lista3 = entrada[terco2:]
    lista = [lista1, lista2, lista3]
    return lista


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
r1, r2, r3 = func(lista)

print(r1, r2, r3)
