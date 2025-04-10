/*
E05
Apresente a query para listar o nome dos autores que publicaram livros através de editoras
NÃO situadas na região sul do Brasil. 
Ordene o resultado pela coluna nome, em ordem crescente.
Não podem haver nomes repetidos em seu retorno.
*/

SELECT a.nome
FROM autor a
LEFT JOIN livro l
ON a.codautor = l.autor
LEFT JOIN editora ed
ON l.editora = ed.codeditora
LEFT JOIN endereco en
ON ed.endereco = en.codendereco
WHERE en.estado not in ('PARANÁ')
GROUP BY a.nome
ORDER BY a.nome