import hashlib

executando = True

while executando:
    entrada = input("Digite um texto ou 'sair' para encerrar: ")
    if entrada.strip().lower() == 'sair':
        print('Encerrando...')
        executando = False
    else:
        cod_hash = hashlib.sha1(entrada.encode())
        print('Resultado do SHA-1:')
        print(cod_hash.hexdigest())
