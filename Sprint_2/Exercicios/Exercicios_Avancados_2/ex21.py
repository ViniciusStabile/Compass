"""
Utilizando high order functions, implemente o corpo da função conta_vogais. 
O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.

É obrigatório aplicar as seguintes funções:

len
filter
lambda
"""


def conta_vogais(texto: str) -> int:
    vogais = ['a', 'e', 'i', 'o', 'u']
    letras = list(texto.lower())
    qtdVogais = list(filter(lambda x: x in vogais, letras))
    return len(qtdVogais)


print(conta_vogais('Ola mundo, este e um importante teste'))
