/*
Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV. 
Utilizar o caractere ';' (ponto e vírgula) como separador. 
Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e
seus respectivos nomes de cabeçalho que listamos abaixo:
CodLivro, Título, CodAutor, NomeAutor, Valor, CodEditora, NomeEditora
Observação: O arquivo exportado, conforme as especificações acima, deve ser disponibilizado no GitHub

*/

SELECT l.cod AS CodLivro, l.titulo as Titulo,
	   l.autor AS CodAutor, a.nome AS NomeAutor,
       l.valor AS Valor, l.editora as CodEditora, 
       e.nome as NomeEditora
FROM livro l 
INNER JOIN autor a  
ON l.autor = a.codautor
inner join editora e 
ON l.editora = e.codeditora
ORDER BY l.valor DESC
LIMIT 10
