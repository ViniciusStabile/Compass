with open('actors.csv', 'r') as f:
    linhas = f.readlines()

cabecalho = linhas[0].strip().split(',')
dados = [linha.strip().split(',') for linha in linhas[1:]]

dados[4] = ["Robert Downey Jr.", '3947.30 ',
            '53',  '74.50 ', 'The Avengers', '623.40']

# etapa 1
ator_mais_filmes = ''
quantidade_filmes = 0

for linha in dados:
    ator = linha[0]
    num_filmes = int(linha[2])

    if num_filmes > quantidade_filmes:
        quantidade_filmes = num_filmes
        ator_mais_filmes = ator

print('-' * 40)

print(
    f"O ator que mais possui filmes no dataset é {ator_mais_filmes} com {quantidade_filmes} filmes.")

print('-' * 40)
# etapa 2

soma = 0
for linha in dados:
    soma += float(linha[5])

media = soma / len(dados)

print(
    f'A media de receita de bilheteria bruta dos principais filmes é {media:.2f} milhões de dolares')

print('-' * 40)
# etapa 3

ator_maior_media = ''
maior_media = 0.0

for linha in dados:
    media = float(linha[3])

    if media > maior_media:
        ator_maior_media = linha[0]
        maior_media = media

print(
    f'O ator com maior média de receita de bilheteria bruta por filme é {ator_maior_media} com uma media de {maior_media:.2f} milhoes de dolares')

print('-' * 40)
# etapa 4

contagem_filmes = {}

for linha in dados:
    filme = linha[4]

    if filme in contagem_filmes:
        contagem_filmes[filme] += 1
    else:
        contagem_filmes[filme] = 1

filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))

for i, (filme, quantidade_aparicoes) in enumerate(filmes_ordenados, start=1):
    print(f'({i}) - O filme {filme} aparece {quantidade_aparicoes} vez(es) no dataset.')

print('-' * 40)
# etapa 5

lista_ator_receita_bruta = []

for linha in dados:
    ator = linha[0]
    receita = float(linha[1])
    lista_ator_receita_bruta.append((ator, receita))

lista_ator_receita_bruta.sort(key=lambda x: -x[1])

for ator, receita in lista_ator_receita_bruta:
    print(f"{ator} - ({receita:.2f})")
