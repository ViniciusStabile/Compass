"""
Você foi encarregado de desenvolver uma nova feature  para um sistema de gestão de supermercados. 
O analista responsável descreveu o requisito funcional da seguinte forma:

- Para realizar um cálculo de custo, o sistema deverá permitir filtrar um determinado conjunto de produtos, 
de modo que apenas aqueles cujo valor unitário for superior à média deverão estar presentes no resultado. 
Vejamos o exemplo:

Conjunto de produtos (entrada):

Arroz: 4.99
Feijão: 3.49
Macarrão: 2.99
Leite: 3.29
Pão: 1.99

"""


def maiores_que_media(conteudo: dict) -> list:
    media = sum(conteudo.values()) / len(conteudo)
    valor_acima_media = []
    for item, valor in conteudo.items():
        if valor > media:
            valor_acima_media.append((item, valor))
    valor_acima_media.sort(key=lambda x: x[1])
    return valor_acima_media


conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

resultado = maiores_que_media(conteudo)
