texto = sc.textFile("README.md")
palavras = texto.flatMap(lambda linha: linha.split())
palavras_filtradas = palavras.filter(lambda p: p.strip() != "")
palavras_minusculas = palavras_filtradas.map(lambda p: p.lower())
contagem = palavras_minusculas.map(
    lambda p: (p, 1)).reduceByKey(lambda x, y: x + y)
contagem.collect()
