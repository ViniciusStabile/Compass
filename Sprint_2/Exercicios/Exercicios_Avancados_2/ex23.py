"""
A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. 
Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), 
as quais devem ser aplicadas à lista de operadores nas respectivas posições. 
Após aplicar cada operação ao respectivo par de operandos, 
a função deverá retornar o maior valor dentre eles.

Na resolução da atividade você deverá aplicar as seguintes funções:

max
zip
map
"""

import operator


def calcular_valor_maximo(operadores, operandos):
    operacoes = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod
    }

    resultados = map(
        lambda x: operacoes[x[0]](x[1][0], x[1][1]),
        zip(operadores, operandos)
    )

    return max(resultados)


operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]
