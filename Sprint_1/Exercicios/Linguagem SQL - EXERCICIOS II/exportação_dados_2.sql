/*
Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na biblioteca para um arquivo CSV. 
Utilizar o caractere pipe () como separador. 
Lembre-se que o conteúdo do arquivo deve seguir a sequência de colunas e
seus respectivos nomes de cabeçalho listados abaixo: CodEditora, NomeEditora, QuantidadeLivros. 
Observação: O arquivo exportado, conforme as especificações acima, deve ser disponibilizado no GitHub.

*/

SELECT l.editora as CodEditora,e.nome as NomeEditora, count(*) as QuantidadeLivros
FROM livro l 
inner join editora e 
ON l.editora = e.codeditora
GROUP BY e.nome
LIMIT 5
