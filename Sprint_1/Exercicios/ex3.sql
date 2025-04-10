/*
E03
 Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
 O resultado deve conter apenas as colunas quantidade, nome, estado e cidade.
  Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.
*/

SELECT count(*) as quantidade, ed.nome,en.estado,en.cidade
FROM livro l
LEFT JOIN editora ed
ON l.editora = ed.codeditora
LEFT JOIN endereco en
ON ed.endereco = en.codendereco
GROUP BY ed.nome
ORDER BY quantidade desc
LIMIT 5