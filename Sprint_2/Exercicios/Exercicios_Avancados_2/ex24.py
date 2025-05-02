"""
Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. 
Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, 
no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.

Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo 
as seguintes informações:

Nome do estudante
Três maiores notas, em ordem decrescente
Média das três maiores notas, com duas casas decimais de precisão

O resultado do processamento deve ser escrito na saída padrão (print), 
ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:

Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>
"""

import csv

estudantes = []

with open('estudantes.csv', newline='') as f:
    leitor = csv.reader(f)
    for linha in leitor:
        nome = linha[0]
        notas = list(map(int, linha[1:]))

        maiores_notas = sorted(notas, reverse=True)[:3]
        media_maiores = round(sum(maiores_notas) / 3, 2)

        estudantes.append({
            'nome': nome,
            'maiores_notas': maiores_notas,
            'media': media_maiores
        })

estudantes.sort(key=lambda x: x['nome'])

for e in estudantes:
    print(
        f"Nome: {e['nome']} Notas: {e['maiores_notas']} Média: {e['media']:.2f}")
