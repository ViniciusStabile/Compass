/*
E06
Apresente a query para listar o autor com maior número de livros publicados. 
O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.
*/

SELECT a.codautor , a.nome, count(a.nome) as quantidade_publicacoes
FROM autor a
LEFT JOIN livro l 
ON a.codautor = l.autor
GROUP BY nome
ORDER BY quantidade_publicacoes DESC
LIMIT 1